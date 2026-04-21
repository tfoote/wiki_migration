import collections
import os
import re

input_file = "current_pages.yaml"

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit(1)

macro_counts = collections.Counter()

# Regex to find macros: <<Name(args)>> or <<Name>>
# Macro name starts with letter, followed by letters or numbers or underscores.
macro_pattern = re.compile(r"<<([a-zA-Z][a-zA-Z0-9_]*)(\(.*\))?>>")

count = 0
with open(input_file, "r") as f:
    for line in f:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            value = parts[1].strip('"')
            src_file = value
            if os.path.exists(src_file):
                count += 1
                try:
                    with open(src_file, "r", errors="ignore") as f_in:
                        content = f_in.read()
                        matches = macro_pattern.findall(content)
                        for match in matches:
                            macro_name = match[0]
                            macro_counts[macro_name] += 1
                except Exception as e:
                    print(f"Error reading {src_file}: {e}")

print(f"Scanned {count} files.")
print("Macro Prevalence:")
for name, count in macro_counts.most_common():
    print(f"{name}: {count}")
