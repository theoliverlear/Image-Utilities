import numpy as np
import cv2 as cv
from ImageArray import ImageArray
class ImageStream:
    #-----------------------------Constructor---------------------------------
    def __init__(self):
        # The constructor takes no arguments. It starts you with a basic
        # webcam, videoCodex, and videoRecorder. This is all you need to start
        # streaming images into Python. By default, the stream() method is
        # called to instantly start the stream.
        # TODO: Add functionality to allow for the user to choose when to
        #       start the stream.
        webcam = cv.VideoCapture(0)
        videoCodec = cv.VideoWriter_fourcc(*"XVID")
        videoRecorder = cv.VideoWriter("output.avi", videoCodec, 30, (640, 480))
        self.stream(webcam, videoRecorder)
    #----------------------------Image-Stream---------------------------------
    def stream(self, camera, videoRecorder):
        # This method starts the data capture from the webcam. It takes the
        # camera data which gives a single image and a boolean for if the
        # image is able to continue. The raw stream is called "Input" and the
        # stream with the RGB values is called "Stream". The RGB values are
        # printed to the console with the printStream() method. The loop will
        # continue until the space bar is pressed. An 8-bit integer is used to
        # ensure that the input will be read correctly in an 8-bit format.
        while True:
            hasNext, img = camera.read()
            if hasNext:
                rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                videoRecorder.write(img)
                cv.imshow("Input", img)
                cv.imshow("Stream", rgb)
                imgArray = ImageArray(np.array(rgb))
                self.printStream(imgArray)
                isSpaceBarBuffered = cv.waitKey(1) & 0xFF # Change to 0 for
                                                          # default computer
                                                          # camera
                if isSpaceBarBuffered == 32:  # 32 is code for space bar
                    break
            else:
                break
        camera.release()
        videoRecorder.release()
        cv.destroyAllWindows()
    #--------------------------Print-Stream-Data------------------------------
    def printStream(self, imgArray):
        # This method takes an image as an array and prints its RGB values.
        print(imgArray.getImageData().getRGB())
