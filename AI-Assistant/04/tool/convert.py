import re

input_file = "input.md"
output_file = "input.txt"

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

with open(output_file, "w") as txt_file:
    txt_file.write("\n".join(output_lines))



# Parse input.txt and store tags and their corresponding content in a dictionary
with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

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
with open('output.html', 'w', encoding='utf-8') as output_file:
    output_file.write(template)