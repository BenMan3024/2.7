from PIL import Image
import datetime
import os


def string_handler(params):
    print(f"Server response:\n\t{params[0]}")
    return params[1:]


def image_handler(params: Image.Image):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    desktop = os.path.join(os.path.expanduser("~/OneDrive"), "Desktop")
    screenshots_directory = os.path.join(desktop, "Server_ScreenShots")
    try:
        os.mkdir(screenshots_directory)
    except FileExistsError:
        pass
    with open(os.path.join(screenshots_directory, f"{time}.png"), "wb") as file:
        file.write(params)
    print(f"Server response:\n\t The screenshot wait at {screenshots_directory}.")


