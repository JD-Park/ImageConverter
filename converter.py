from PIL import Image
import os

"""Iterate through each image and convert to desired type."""
"""Save the file names to a list and name the converted images similarly."""

directory = 'Images'
directory_contents = os.listdir(directory)

files_to_convert = []
 
for contents in directory_contents:
    files_to_convert.append(Image.open('Images/' + contents))

print(files_to_convert)    

for i, files in enumerate(files_to_convert):
    files.save((f'Converted/new_{i}.ico'), 'ICO', SAVE_ALL=True, sizes=[(128, 128)])
    