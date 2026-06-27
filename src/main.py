import os
import shutil
from textnode import TextNode
from textnode import TextType
from gen_content import generate_page
from gen_content import generate_pages_recursive

dir_path_content = "./content"
template_path = "./template.html"
dir_path_public = "./docs"

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_recursive("static", "public")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

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
    

        