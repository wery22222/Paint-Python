#imports files 
import regular
import rectangle

dimension = [] # List which stores the inputs
shapeType=input("regular(r) or rectangle(i)")# Selects one of the 2 options
if  shapeType.upper() == 'R': # checks option 1
    r = 0
    regularShapeList = ["", "", ""]#setsup the list to store values
    regularInput = input("Type in: the height,the radius,the number of sides with a '/' between dimensions")#takes the input
    for i in range(3):#loops through elements of the list
         while r<len(regularInput):#makes sure doesn't og over inputed number
             if regularInput[r] == "/":#checks if element check is '/'
                 r+=1 #iterates
                 break
             elif regularInput[r].isdigit():#checks if digit
                regularShapeList[i]= regularShapeList[i]+regularInput[r]#concatenates to current element
                r+=1#iterates
             else:
                 r+=1#iterates
    #turns all elements into Floats
    for i in range(len(regularShapeList)):
        regularShapeList[i] = float(regularShapeList[i])
    #creates object to calculate and sets to variable
    whatIsNeeded = regular.calculate_regular(regularShapeList)
    print(f"""The area of the floor is {whatIsNeeded.IMPORTANTdETAILS[0]}
The amount of paint required to paint the walls is the equivelant of {whatIsNeeded.IMPORTANTdETAILS[1]}
The volume of the room is {whatIsNeeded.IMPORTANTdETAILS[2]}
The surface area of the room is {whatIsNeeded.IMPORTANTdETAILS[3]}""")#prints the details

elif shapeType.upper() == 'I':#selects rectangle case
    r = 0
    rectangleShapeList = ["", "", ""]#setsup the list to store values
    rectangleInput = input("Type in: the height,the width,the length with a '/' between dimensions")#takes input
    for i in range(3):#loops through elements of the list
        while r < len(rectangleInput):#makes sure doesn't og over inputed number
            if rectangleInput[r] == "/"::#checks if element check is '/'
                r += 1#iterates
                break
            elif rectangleInput[r].isdigit():#checks if number the adds to list
                rectangleShapeList[i] = rectangleShapeList[i] + rectangleInput[r]
                r += 1#iterates
            else:
                r += 1#iterates
    for i in range(len(rectangleShapeList)):#sets all elements to floats
        rectangleShapeList[i] = float(rectangleShapeList[i])

    whatIsNeeded = rectangle.Rectangle(rectangleShapeList)#calls a new object to calculate all the values for a rectangle (case I)
    print(f"""The area of the floor is {whatIsNeeded.IMPORTANTdETAILS[0]}#prints the details
The amount of paint required to paint the walls is the equivelant of {whatIsNeeded.IMPORTANTdETAILS[1]}
The volume of the room is {whatIsNeeded.IMPORTANTdETAILS[2]}
The surface area of the room is {whatIsNeeded.IMPORTANTdETAILS[3]}""")
