import os

from PIL import Image
from tkinter import filedialog

"""Iterate through each image and convert."""
"""Save each converted files with a new name."""

"""Allow user to select the input and output folder. No dialogue currently."""
path = filedialog.askdirectory(initialdir="/")
save = filedialog.askdirectory()

"""Read the contents of the input folder."""
path_contents = os.listdir(path)

"""Create variables for resizing image and creating the ICO"""
width, height = 256, 256
sizes = [(256, 256)]

"""Create an empty list for resized and converted images."""
resized = []

def lower_case(path_contents):
    """Make all files in the input folder lowercase."""
    path_contents_lower = [string.lower() for string in path_contents]
    return path_contents_lower

"""Assign files from lower case function to a new list."""
path_contents_lower = lower_case(path_contents)

"""Iterate through the lower case list and only select file with the specified extensions."""
for contents in path_contents_lower:
    if (contents.endswith(".png") or contents.endswith(".jpg") or contents.endswith(".jpeg")
        or contents.endswith(".bmp")):
        """Open the image."""
        image = Image.open((f'{path}/' + contents))
        """Convert to RGBA."""
        rgba = image.convert('RGBA')
        """Resize the image and add to resized list."""
        resized.append(rgba.resize((width, height), resample=0))       

"""Iterate through the images added to the resized list and save them as an ICO."""
for i, files in enumerate(resized):
    files.save((f'{save}/new_{i}.ico'), 'ICO', SAVE_ALL=True, sizes=sizes, bits=(32, 32))

