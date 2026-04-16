import os

pages_dir = "pages"
output_file = "current_pages.yaml"

result = {}

if not os.path.exists(pages_dir):
    print(f"Error: {pages_dir} directory not found.")
    exit(1)

for item in os.listdir(pages_dir):
    if "(2f)" in item:
        continue

    item_path = os.path.join(pages_dir, item)

    if os.path.isdir(item_path):
        current_file_path = os.path.join(item_path, "current")
        if os.path.exists(current_file_path):
            try:
                with open(current_file_path, "r") as f:
                    current_version = f.read().strip()

                revisions_path = os.path.join(item_path, "revisions")
                actual_file_path = os.path.join(revisions_path, current_version)

                if os.path.exists(actual_file_path):
                    try:
                        with open(actual_file_path, "r", errors="ignore") as f_in:
                            if "CategoryPackage" in f_in.read():
                                # Use relative path from workspace root
                                result[item] = actual_file_path
                    except Exception as e:
                        print(f"Error reading {actual_file_path}: {e}")
                else:
                    print(f"Warning: Resourced file {actual_file_path} not found for {item}")
            except Exception as e:
                print(f"Error reading {current_file_path}: {e}")
        else:
            print(f"Warning: No 'current' file in {item_path}")

with open(output_file, "w") as f:
    for key, value in sorted(result.items()):
        # Quoting to handle special characters safely
        f.write(f'"{key}":\n')
        f.write(f'  source_file: "{value}"\n')

print(f"Successfully generated {output_file} with {len(result)} entries.")
