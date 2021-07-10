import PIL
from PIL import Image
from numpy import asarray

print('Pillow Version:', PIL.__version__)

im = Image.open("./images/ascii-pineapple.jpg")

data = asarray(im)
print(type(data))
print(data)