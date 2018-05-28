#!/usr/bin/python
from PIL import Image
import sys

borderRatio = 11.52

image = Image.open(sys.argv[1]);
print image.size

newSize = (image.size[0] + int(round(image.size[0] / borderRatio)),
    image.size[1] + int(round(image.size[1] / borderRatio)))
print newSize

newImage = Image.new("RGB", newSize, (255, 255, 255))
newImage.paste(image, ((newImage.size[0] - image.size[0]) / 2, (newImage.size[1] - image.size[1]) / 2))
