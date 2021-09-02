# Third party modules
import numpy as np
from PIL import Image


def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "RGBA":
        channels = 4
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((width, height, channels))
    return pixel_values

print("Welcome to the LEGO to DOT converter")
image = get_image("test_image.png")

col_names = ('R','G','B','A')
image = np.array(image, dtype = [(n,'int16') for n in col_names])

print(image[0])
print(image.shape)
#print(image.shape)
print("Thanks")