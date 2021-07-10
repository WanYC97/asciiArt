import PIL
from PIL import Image
from numpy import asarray

print('Pillow Version:', PIL.__version__)

im = Image.open("./images/ascii-pineapple.jpg")

data = asarray(im)
print(type(data))
print(data[0][0])

for x in range(len(data)):
    for y in range(len(data[x])):
        pixel = data[x][y]
        