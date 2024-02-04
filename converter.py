import os
import tkinter as tk

from PIL import Image
from tkinter import filedialog

"""Iterate through each image and convert to desired type."""
"""Save the converted files with new names."""

path = filedialog.askdirectory(initialdir="/")
path_contents = os.listdir(path)

print(path)
print(path_contents)

# def convert():
files_to_convert = []

for contents in path_contents:
    if (contents.endswith(".PNG") or contents.endswith(".JPG") or contents.endswith(".JPEG")
        or contents.endswith(".BMP") or contents.endswith(".png") or contents.endswith(".jpeg")
        or contents.endswith(".jpg") or contents.endswith(".bmp")):
        files_to_convert.append(Image.open(f'{path}/' + contents))

# print(files_to_convert)    

for i, files in enumerate(files_to_convert):
    files.save((f'Converted/new_{i}.ico'), 'ICO', SAVE_ALL=True, sizes=[(128, 128)])
    
# convert()    