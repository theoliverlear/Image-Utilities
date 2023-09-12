import os.path
from PIL import Image
import numpy as np
from ImageFile import ImageFile
from ImageStream import ImageStream
#------------------------------------Main-------------------------------------
def main():
    # Read image from file into ImageFile object. The object stores the image
    # as a copy and contains the data of the colors in the image as a
    # ImageData object.
    #--------------------------View-Color-Count-------------------------------
    # Create an image file which creates an ImageData object. The ImageData
    # object copies the image and turns it into an array. The RGB values are
    # extracted from the array and stored in the ImageData object. Each step
    # is printed to see the process.
    imgFile = ImageFile("img.jpg")
    imgFileData = imgFile.getImageData()
    print(imgFileData)    # Prints toString
    imgDataTotals = imgFile.getImageData().getRGB()
    print(imgDataTotals)  # Prints RGB totals
    #----------------------------Random-Number--------------------------------
    randInt = np.random.randint(0, 2)
    print(f"Random number: {imgDataTotals[randInt]}")
    #-----------------------------Image-Stream--------------------------------
    # Start the image stream. The image stream takes the image from the webcam
    # instead of a static image. The image stream is a continuous stream of
    # random numbers. This is the main functionality intended for the hexbugs
    # research.
    print("Starting image stream. This may take a moment Press space bar"
          " to stop.")
    imgStream = ImageStream()
main()
#-----------------------------------Notes-------------------------------------
# TODO: Find consistent letter case styling -- since the program
#       is written for objects at the current moment, it is
#       will be camelCase like other OOP languages.

#TODO: Find out if data can be read asynchronusly. If so, then the frames
#      can be read and processed at the same time. Then the program will have
#      a consistent stream of data for random number generation.