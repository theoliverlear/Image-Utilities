class ImageData:
    #-----------------------------Constructor---------------------------------
    def __init__(self, r, g, b):
        # Takes RGB values and stores them. The values can be accessed for
        # random number generation. Future functionality will implement
        # various algorithms and mutations to the RGB values.
        self.r = r
        self.g = g
        self.b = b
    #------------------------------To-String----------------------------------
    def __str__(self):
        return f"Red: {self.r}, Green: {self.g}, Blue: {self.b}"
    #-------------------------------Getters-----------------------------------
    # TODO: Find out if Java encapsulation is necessary in Python
    def getRed(self):
        return self.r
    def getGreen(self):
        return self.g
    def getBlue(self):
        return self.b
    def getRGB(self):
        return [self.r, self.g, self.b]
