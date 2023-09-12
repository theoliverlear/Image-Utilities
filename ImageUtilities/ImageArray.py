import numpy as np
from ImageData import ImageData
class ImageArray:
    #-----------------------------Constructor---------------------------------
    def __init__(self, imgArray):
        # Takes an image array and loops through it to add up the RGB values.
        # The total RGB values are stored in an ImageData object. These
        # numbers are used for random number generation.
        self.imgArray = imgArray
        self.imgArray = np.array(self.imgArray) # Regular array to numpy array
        r, g, b = 0, 0, 0
        for i in range(len(self.imgArray)):
            for j in range(len(self.imgArray[i])):
                r += self.imgArray[i][j][0]
                g += self.imgArray[i][j][1]
                b += self.imgArray[i][j][2]
        self.imageData = ImageData(r, g, b)
    #-------------------------------Getters-----------------------------------
    def getImageArray(self):
        return self.imgArray
    def getImageData(self):
        return self.imageData