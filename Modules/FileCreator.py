import os


def create_file(text, index):
    folder = "source"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = f"{folder}/index{index}.html"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"File {file_path} created!")
