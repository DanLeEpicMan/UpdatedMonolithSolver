import os
from os.path import join, exists
import sys

# All this script does is execute the other scripts with the correct arguments. In other words, this streamlines the process from the user running two scripts to just running one script.

# This script may also seem very lazy and non-Pythonic. While this is mostly true, Anaconda was giving me a hard time with the module system, so I figured that executing the other scripts via terminal (as opposed to importing them) is the best solution.

image = None
try:
    image = sys.argv[1]
    image = image if (image.endswith(".png") or image.endswith(".jpg")) else image + ".png" # Adds .png by default since Windows Snippet Tool saves images as PNGs by default. A bit lazy of me I know
except IndexError: # In case the user forgets to provide an image.
    sys.exit("Please provide a reference image")


if not (exists(join("screenshots", image))):
    print("Image not found. Did you input the correct name? Try copying the name (with extention) and pasting it here. Right click to paste.")
else:
    test = os.system("python parser.py -o " + join("boards", "out.csv") + " " + join("screenshots", image))
    if (test != 0): 
        print("Something went wrong in the automatic conversion process. Try running the script again, and if the problem persists you may have to manually create the board. Contact danleman1337 (Discord) for any assistance.")
    else:
        os.system("python THM.py out")
