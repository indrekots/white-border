#!/usr/bin/python
from PIL import Image
import sys, os

borderRatio = 11.52
whiteBorderFolder = 'whiteBorder'

def isJpeg(fileName):
    return '.jpg' in fileName or '.jpeg' in fileName

def addWhiteBorder(fileName):
    image = Image.open(fileName);

    newSize = (image.size[0] + int(round(image.size[0] / borderRatio)),
    image.size[1] + int(round(image.size[1] / borderRatio)))

    print 'Adding a white border to ' + fileName
    newImage = Image.new("RGB", newSize, (255, 255, 255))
    newImage.paste(image, ((newImage.size[0] - image.size[0]) / 2, (newImage.size[1] - image.size[1]) / 2))

    if not os.path.exists(whiteBorderFolder):
        os.makedirs(whiteBorderFolder)

    newImage.save(whiteBorderFolder + '/' + fileName)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if isJpeg(f):
        addWhiteBorder(f)
