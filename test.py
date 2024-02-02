import os
import re

def remove_layout_block_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the pattern to remove the layout block
    pattern_to_remove = re.compile(r'---\nlayout: default\n---\n?')
    
    # Remove the pattern
    new_content = re.sub(pattern_to_remove, '', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                remove_layout_block_in_file(os.path.join(root, file))

# Replace with the directory you want to process
process_directory('.')
