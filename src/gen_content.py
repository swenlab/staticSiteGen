import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip(" ")
            return title
    raise Exception("no note found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path)
    contents = f.read()
    f.close()
    f = open(template_path)
    template = f.read()
    f.close()
    html_string = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)
    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    result = result.replace('href="/','href="' + basepath).replace('src="/', 'src="' + basepath)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    f = open(dest_path, "w")
    f.write(result)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)