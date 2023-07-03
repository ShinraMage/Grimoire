import re
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description='Markdown to HTML converter.')
parser.add_argument('-i', '--input', type=str, help='Input markdown file')

# Parse the command-line arguments
args = parser.parse_args()

input_file = args.input
output_file = args.input.replace('.md', '.html')

with open(input_file, 'r', encoding='utf-8') as md_file:
    lines = md_file.readlines()

output_lines = []

for line in lines:
    if line.startswith("##"):
        parsed_line = "{{" + line[2:].strip() + "}}"
    elif line.startswith("*"):
        parsed_line = line.strip() + "<br>"
    else:
        parsed_line = line.strip()

    output_lines.append(parsed_line)

input_text = ' '.join(output_lines)  # Convert list to a single string

pattern = r'\{\{(.*?)\}\}(.*?)(?=\{\{(.*?)\}\}|$)'
matches = re.findall(pattern, input_text, re.DOTALL)

tag_dict = {}
for match in matches:
    tag = match[0].strip()
    content = match[1].strip()
    tag_dict[tag] = content

# Parse template.html and replace tags with their corresponding content
with open('template.html', 'r', encoding='utf-8') as template_file:
    template = template_file.read()

pattern = r'\{\{(.*?)\}\}'
matches = re.findall(pattern, template)

for match in matches:
    tag = match.strip()
    if tag in tag_dict:
        template = template.replace('{{' + tag + '}}', tag_dict[tag])

# Save the updated template as output.html
with open(output_file, 'w', encoding='utf-8') as html_file:
    html_file.write(template)