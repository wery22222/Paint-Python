import regular
import rectangle

dimension = [] # List which stores the inputs
shapeType=input("regular(r) or rectangle(i)")
if  shapeType.upper() == 'R':
    r = 0
    regularShapeList = ["", "", ""]
    regularInput = input("Type in: the height,the radius,the number of sides with a '/' between dimensions")
    for i in range(3):
         while r<len(regularInput):
             if regularInput[r] == "/":
                 r+=1
                 break
             elif regularInput[r].isdigit():
                regularShapeList[i]= regularShapeList[i]+regularInput[r]
                r+=1
             else:
                 r+=1
    for i in range(len(regularShapeList)):
        regularShapeList[i] = float(regularShapeList[i])

    whatIsNeeded = regular.calculate_regular(regularShapeList)
    print(f"""The area of the floor is {whatIsNeeded.IMPORTANTdETAILS[0]}
The amount of paint required to paint the walls is the equivelant of {whatIsNeeded.IMPORTANTdETAILS[1]}
The volume of the room is {whatIsNeeded.IMPORTANTdETAILS[2]}
The surface area of the room is {whatIsNeeded.IMPORTANTdETAILS[3]}""")

elif shapeType.upper() == 'I':
    r = 0
    rectangleShapeList = ["", "", ""]
    rectangleInput = input("Type in: the height,the width,the length with a '/' between dimensions")
    for i in range(3):
        while r < len(rectangleInput):
            if rectangleInput[r] == "/":
                r += 1
                break
            elif rectangleInput[r].isdigit():
                rectangleShapeList[i] = rectangleShapeList[i] + rectangleInput[r]
                r += 1
            else:
                r += 1
    for i in range(len(rectangleShapeList)):
        rectangleShapeList[i] = float(rectangleShapeList[i])

    whatIsNeeded = rectangle.Rectangle(rectangleShapeList)
    print(f"""The area of the floor is {whatIsNeeded.IMPORTANTdETAILS[0]}
The amount of paint required to paint the walls is the equivelant of {whatIsNeeded.IMPORTANTdETAILS[1]}
The volume of the room is {whatIsNeeded.IMPORTANTdETAILS[2]}
The surface area of the room is {whatIsNeeded.IMPORTANTdETAILS[3]}""")
