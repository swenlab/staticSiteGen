import os
import sys
import shutil
from textnode import TextNode
from textnode import TextType
from gen_content import generate_page
from gen_content import generate_pages_recursive

dir_path_content = "./content"
template_path = "./template.html"
dir_path_public = "./docs"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("docs")
    copy_recursive("static", "docs")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

def copy_recursive(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            print(f"Copying {source_path} -> {destination_path}")
            shutil.copy(source_path, destination_path)
        else:
            os.mkdir(destination_path)
            copy_recursive(source_path, destination_path)

if __name__ == "__main__":
    main()
    

        