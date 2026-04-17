import sys
import yaml
import rosdistro
import urllib.request
import urllib.error
import json
import time
import os
import xml.etree.ElementTree as ET


def github_api_request(url):
    token = os.environ.get("GITHUB_TOKEN")
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            if token:
                headers["Authorization"] = f"token {token}"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    return json.loads(response.read().decode())

        except urllib.error.HTTPError as e:
            if e.code in [403, 429]:
                reset_time = e.headers.get('X-RateLimit-Reset')
                if reset_time:
                    reset_time = int(reset_time)
                    sleep_time = reset_time - time.time() + 5  # Add 5 seconds buffer
                    if sleep_time > 0:
                        print(f"  Rate limit hit. Sleeping for {sleep_time:.2f} seconds...")
                        time.sleep(sleep_time)
                        continue
                else:
                    print(f"  Rate limit hit but no reset header. Sleeping for 60 seconds...")
                    time.sleep(60)
                    continue
            else:
                print(f"  HTTP Error: {e.code}")
                raise e
        except Exception as e:
            print(f"  Error: {e}")
            raise e


def correlate(yaml_file):
    print(f"Loading {yaml_file}...")
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    if not data:
        print("Empty YAML file.")
        return

    print("Loading rosdistro index...")
    index_url = rosdistro.get_index_url()
    index = rosdistro.get_index(index_url)
    print("Loading noetic distribution...")
    distro = rosdistro.get_distribution(index, "noetic")

    token = os.environ.get("GITHUB_TOKEN")
    repo_archived_cache = {}


    for pkg_name in data:
        print(f"\nProcessing package: {pkg_name}")
        found = False
        
        # Find package in distro
        for repo_name, repo in distro.repositories.items():
            # Check release_repository which has package_names list
            if repo.release_repository and pkg_name in repo.release_repository.package_names:
                found = True
                print(f"  Found in repository: {repo_name}")
                
                repo_url = None
                branch = "noetic"
                
                if repo.source_repository:
                    repo_url = repo.source_repository.url
                    if repo.source_repository.version:
                        branch = repo.source_repository.version
                elif repo.release_repository:
                    repo_url = repo.release_repository.url
                    print(f"  Warning: Source repo not found, using release repo: {repo_url}")

                # Determine subdirectory
                subdir = ""
                if len(repo.release_repository.package_names) > 1:
                    subdir = pkg_name
                    print(f"  Assuming subdirectory: {subdir} (multi-package repo)")
                else:
                    subdir = ""
                    print("  Assuming package is at project root.")

                # Check for README.md
                readme_exists = False
                if repo_url and "github.com" in repo_url:
                    # Convert git URL to raw content URL
                    base_url = (
                        repo_url.replace(".git", "")
                        .replace("https://github.com/", "https://raw.githubusercontent.com/")
                        .replace("http://github.com/", "https://raw.githubusercontent.com/")
                    )
                    
                    readme_url = f"{base_url}/{branch}/"
                    if subdir:
                        readme_url += f"{subdir}/"
                    readme_url += "README.md"

                    print(f"  Checking README at: {readme_url}")
                    try:
                        req = urllib.request.Request(readme_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req) as response:
                            if response.status == 200:
                                readme_exists = True
                                print("  README found!")
                    except urllib.error.HTTPError as e:
                        if e.code == 404:
                            print("  README not found (404).")
                        else:
                            print(f"  HTTP Error checking README: {e.code}")
                    except Exception as e:
                        print(f"  Error checking README: {e}")
                else:
                    print("  Skipping README check (not GitHub or no repo URL).")

                # Check package.xml
                package_xml_match = False
                if repo_url and "github.com" in repo_url:
                    package_xml_url = f"{base_url}/{branch}/"
                    if subdir:
                        package_xml_url += f"{subdir}/"
                    package_xml_url += "package.xml"

                    print(f"  Checking package.xml at: {package_xml_url}")
                    try:
                        req = urllib.request.Request(package_xml_url, headers={'User-Agent': 'Mozilla/5.0'})
                        if token:
                            req.add_header("Authorization", f"token {token}")
                        with urllib.request.urlopen(req) as response:
                            if response.status == 200:
                                xml_content = response.read()
                                root = ET.fromstring(xml_content)
                                name_tag = root.find('name')
                                if name_tag is not None and name_tag.text.strip() == pkg_name:
                                    package_xml_match = True
                                    print("  package.xml match!")
                                else:
                                    print(f"  package.xml mismatch! Found: {name_tag.text if name_tag is not None else 'None'}")
                    except urllib.error.HTTPError as e:
                        if e.code == 404:
                            print("  package.xml not found (404).")
                        else:
                            print(f"  HTTP Error checking package.xml: {e.code}")
                    except Exception as e:
                        print(f"  Error checking package.xml: {e}")
                else:
                    print("  Skipping package.xml check (not GitHub or no repo URL).")

                data[pkg_name]["package_xml_match"] = package_xml_match

                if not package_xml_match and repo_url and "github.com" in repo_url:
                    print(f"  Package.xml mismatch or not found at guess. Searching repository...")
                    parts = repo_url.replace(".git", "").split("/")
                    if len(parts) >= 2:
                        owner = parts[-2]
                        repo_name_only = parts[-1]
                        tree_url = f"https://api.github.com/repos/{owner}/{repo_name_only}/git/trees/{branch}?recursive=1"
                        print(f"  Fetching file tree from: {tree_url}")
                        try:
                            tree_info = github_api_request(tree_url)
                            if tree_info and "tree" in tree_info:
                                for item in tree_info["tree"]:
                                    path = item.get("path", "")
                                    if path.endswith("package.xml"):
                                        # Construct raw URL to check it
                                        cand_xml_url = f"{base_url}/{branch}/{path}"
                                        try:
                                            req = urllib.request.Request(cand_xml_url, headers={'User-Agent': 'Mozilla/5.0'})
                                            if token:
                                                req.add_header("Authorization", f"token {token}")
                                            with urllib.request.urlopen(req) as response:
                                                if response.status == 200:
                                                    xml_content = response.read()
                                                    root = ET.fromstring(xml_content)
                                                    name_tag = root.find('name')
                                                    if name_tag is not None and name_tag.text.strip() == pkg_name:
                                                        package_xml_match = True
                                                        print(f"  Matched package.xml at: {path}")
                                                        # Subdirectory is the directory containing package.xml
                                                        subdir = "/".join(path.split("/")[:-1])
                                                        print(f"  Updated subdirectory: {subdir}")
                                                        
                                                        # Re-check README at new subdirectory
                                                        cand_readme_url = f"{base_url}/{branch}/"
                                                        if subdir:
                                                            cand_readme_url += f"{subdir}/"
                                                        cand_readme_url += "README.md"
                                                        print(f"  Re-checking README at: {cand_readme_url}")
                                                        readme_exists = False
                                                        try:
                                                            req = urllib.request.Request(cand_readme_url, headers={'User-Agent': 'Mozilla/5.0'})
                                                            with urllib.request.urlopen(req) as response:
                                                                if response.status == 200:
                                                                    readme_exists = True
                                                                    print("  README found at new location!")
                                                        except Exception as e:
                                                            pass # Silent if not found
                                                        
                                                        # Update data
                                                        data[pkg_name]["subdirectory"] = subdir
                                                        data[pkg_name]["readme_exists"] = readme_exists
                                                        data[pkg_name]["package_xml_match"] = True
                                                        break
                                        except Exception as e:
                                            pass # Ignore errors for candidates
                        except Exception as e:
                            print(f"  Error fetching file tree: {e}")

                # Check if archived (GitHub only)


                repository_archived = False
                if repo_url and "github.com" in repo_url:
                    if repo_url in repo_archived_cache:
                        repository_archived = repo_archived_cache[repo_url]
                        print(f"  Archived (cached): {repository_archived}")
                    else:
                        parts = repo_url.replace(".git", "").split("/")
                        if len(parts) >= 2:
                            owner = parts[-2]
                            repo_name_only = parts[-1]
                            api_url = f"https://api.github.com/repos/{owner}/{repo_name_only}"
                            print(f"  Checking archived status at: {api_url}")
                            try:
                                repo_info = github_api_request(api_url)
                                if repo_info:
                                    repository_archived = repo_info.get("archived", False)
                                    print(f"  Archived: {repository_archived}")
                                    repo_archived_cache[repo_url] = repository_archived
                            except Exception as e:
                                print(f"  Error checking archived status after retries: {e}")

                else:
                    print("  Skipping archived check (not GitHub or no repo URL).")

                # Update data
                data[pkg_name]["repository"] = repo_url
                data[pkg_name]["subdirectory"] = subdir
                data[pkg_name]["readme_exists"] = readme_exists
                data[pkg_name]["repository_archived"] = repository_archived
                data[pkg_name]["branch"] = branch
                break  # Found, stop searching repos

        if not found:
            print("  Package not found in rosdistro.")
            data[pkg_name]["unmatched"] = True

    print(f"\nSaving updated data to {yaml_file}...")
    with open(yaml_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=True)
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 correlate_packages.py <yaml_file>")
        sys.exit(1)
    correlate(sys.argv[1])
