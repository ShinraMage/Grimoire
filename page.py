import os
import glob

folders = ["./Setting", "./Novel"]

prepend_text = "---\nlayout: default\n---\n\n"

files_to_update = []
for folder in folders:
    for filename in glob.glob(f"{folder}/**/*.md", recursive=True):
        files_to_update.append(filename)

for filename in files_to_update:
    with open(filename, 'r', encoding='utf8') as f:
        content = f.read()

    # Check if prepend_text already exists at the start of the file
    if not content.startswith(prepend_text):
        content = prepend_text + content
        with open(filename, 'w', encoding='utf8') as f:
            f.write(content)