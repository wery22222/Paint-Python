#importing the libraries
import math

# defining  to line
def sideLength_fromRadius(radius, numberOfSides):#formula for working out outer side length from the radius
    ans = radius*(math.sin(360/numberOfSides))
    ans=ans/(math.sin(90-(180/numberOfSides)))
    return ans

class calculate_regular:
    def floorArea(self):
        return (self.side_length ** 2 * self.numberOfSides) / (4 * math.tan(math.radians(180 / self.numberOfSides)))#the formula for the area of a shape from the side length
    """#################################################
    initialisation of the class
       #################################################
    """
    def __init__(self,shape):
        self.numberOfSides = shape[2]#saves the number of sides
        self.side_length = sideLength_fromRadius(shape[1], shape[2])#stores the side length
        self.areaOfSide =  self.side_length*shape[0]#works out the area of each side
        self.areaOfWalls = self.areaOfSide*shape[2]#works out the total area of the walls
        self.areaOfFloor = self.floorArea()#uses a formula to work out the area of the floor
        self.volume = self.areaOfFloor*shape[0]
        self.totalSurfaceArea = (self.areaOfFloor*2)+self.areaOfWalls
        self.IMPORTANTdETAILS = [self.areaOfFloor,self.areaOfWalls, self.volume,self.totalSurfaceArea]

