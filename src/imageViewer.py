import PySimpleGUI as sg
from PIL import Image, UnidentifiedImageError
import os

layout = [
[
    sg.Text("Choose Image"),
    sg.In(size=(25, 1), enable_events=True, key="-IMAGE-"),
    sg.FileBrowse(file_types=(("PNG", "*.png"), ("JPG", "*.jpg"))),
],
[sg.Image(key = "Image")],
[sg.Button("Close")]]

window = sg.Window("Python Image Editor", layout)

while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    path = sg.popup_get_file("", no_window=True)
    if path == '':
        continue
    
window.close()

