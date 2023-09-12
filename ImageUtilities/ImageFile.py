import numpy as np
from PIL import Image
from ImageData import ImageData
class ImageFile: # TODO: Change class name to not conflict with pillow
    #-----------------------------Constructor---------------------------------
    def __init__(self, path):
        # Takes a path to an image, copies it, and converts it to an array.
        # The array is looped through and the RGB values are added up.
        # The total RGB values are stored in an ImageData object.
        self.path = path
        self.img = Image.open(self.path)
        self.imgCopy = self.img.copy()
        self.imgArray = self.imgCopy.convert("RGB")
        self.imgArray = np.array(self.imgArray)
        r, g, b = 0, 0, 0
        for i in range(len(self.imgArray)):
            for j in range(len(self.imgArray[i])):
                r += self.imgArray[i][j][0]
                g += self.imgArray[i][j][1]
                b += self.imgArray[i][j][2]
        self.imageData = ImageData(r, g, b)
    #-------------------------------Getters-----------------------------------
    # TODO: Find out if Java encapsulation is necessary in Python
    def getImageData(self):
        return self.imageData
    def getImage(self):
        return self.img
    def getImageCopy(self):
        return self.imgCopy
    def getImageArray(self):
        return self.imgArray
    def getImagePath(self):
        return self.path
    #------------------------------To-String----------------------------------
    def __str__(self):
        return f"Image from '{self.path}'"