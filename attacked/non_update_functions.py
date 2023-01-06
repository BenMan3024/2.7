import functions
import inspect
from importlib import reload


def update(request_params: str) -> str:
    with open("functions.py", "w") as file:
        file.write("".join(request_params))
    reload(functions)
    response = 'The file "functions" has been updated'
    return True, "string_handler", [response]


def commands_names(request_params: str) -> list:
    names = dir(functions)
    funcs = []
    for name in names:
        obj = getattr(functions, name)
        if inspect.isfunction(obj):
            funcs.append(name.upper())
    return True, "string_handler", [f"The server commands are : {funcs}"]
