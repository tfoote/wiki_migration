import sys
import yaml
import rosdistro
import urllib.request
import urllib.error
import json

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
                                req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
                                with urllib.request.urlopen(req) as response:
                                    if response.status == 200:
                                        repo_info = json.loads(response.read().decode())
                                        repository_archived = repo_info.get("archived", False)
                                        print(f"  Archived: {repository_archived}")
                                        repo_archived_cache[repo_url] = repository_archived
                            except Exception as e:
                                print(f"  Error checking archived status: {e}")
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
