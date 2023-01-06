import ast


def update_request():
    while True:
        path = input("Type a path to a valid python file (we will not let you send an invalid file:\n\t")
        try:
            with open(path, "r") as python_file:
                file_data = python_file.read()
                ast.parse(file_data)
                return file_data
        except (SyntaxError, FileNotFoundError):
            pass
