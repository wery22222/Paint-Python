class Rectangle:
    def __init__(self, rectangleShapeList):
        self.height = rectangleShapeList[0]#lines 3-5 sets all the values to the object variables
        self.width = rectangleShapeList[1]
        self.length = rectangleShapeList[2]
        self.floorArea = self.width*self.length#works out the floor area
        self.wallArea = (self.height*self.width*2)+(self.length*self.height*2) #works out the wall area
        self.volume = self.height*self.width*self.length # works out the volume
        self.surfaceArea = (self.height*self.width*2)+(self.length*self.height*2)+(self.length*self.width*2)#works out the suface area
        self.IMPORTANTdETAILS = [self.floorArea, self.wallArea, self.volume, self.surfaceArea]#sets all the necessary values to one list for ease of access
