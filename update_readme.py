import os

def get_file_contents(directory="."):
    file_contents = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as f:
                    file_contents += f.read() + "\n\n"
    return file_contents

def update_readme(file_contents):
    with open("README.md", "w") as f:
        f.write("# Repository Contents\n\n")
        f.write("Contents of files:\n\n")
        f.write("```\n")
        f.write(file_contents)
        f.write("```\n")

if __name__ == "__main__":
    contents = get_file_contents()
    update_readme(contents)

