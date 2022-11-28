

class Rectangle:
    def __init__(self, rectangleShapeList):
        self.height = rectangleShapeList[0]
        self.width = rectangleShapeList[1]
        self.length = rectangleShapeList[2]
        self.floorArea = self.width*self.length
        self.wallArea = (self.height*self.width*2)+(self.length*self.height*2)
        self.volume = self.height*self.width*self.length
        self.surfaceArea = (self.height*self.width*2)+(self.length*self.height*2)+(self.length*self.width*2)
        self.IMPORTANTdETAILS = [self.floorArea, self.wallArea, self.volume, self.surfaceArea]
