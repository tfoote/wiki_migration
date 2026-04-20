import yaml

with open("current_pages.yaml", "r") as f:
    data = yaml.safe_load(f)

total = len(data)
matched = 0
unmatched = 0
archived_count = 0

export_data = {}
extend_data = {}

for k, v in data.items():
    is_unmatched = v.get("unmatched", False)
    is_archived = v.get("repository_archived", False)
    
    if is_unmatched:
        unmatched += 1
    elif "repository" in v:
        matched += 1
        if is_archived:
            archived_count += 1

    # Apply filter for lists: must be matched and not archived
    if not is_unmatched and not is_archived:
        if v.get("readme_exists") == True:
            extend_data[k] = v
        else:
            export_data[k] = v


print(f"Total packages: {total}")
print(f"Matched: {matched}")
print(f"Unmatched: {unmatched}")
print(f"Archived (among matched): {archived_count}")
print(f"Exported (no README): {len(export_data)}")
print(f"Extended (has README): {len(extend_data)}")

with open("export_pages.yaml", "w") as f:
    yaml.dump(export_data, f)

with open("extend_pages.yaml", "w") as f:
    yaml.dump(extend_data, f)

