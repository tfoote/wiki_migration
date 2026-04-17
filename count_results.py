import yaml

with open("current_pages.yaml", "r") as f:
    data = yaml.safe_load(f)

total = len(data)
matched = 0
unmatched = 0
archived_count = 0

for k, v in data.items():
    if v.get("unmatched"):
        unmatched += 1
    elif "repository" in v:
        matched += 1
        if v.get("repository_archived"):
            archived_count += 1

print(f"Total packages: {total}")
print(f"Matched: {matched}")
print(f"Unmatched: {unmatched}")
print(f"Archived (among matched): {archived_count}")
