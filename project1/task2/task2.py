#NAME: Brian E. Ramirez Zea
#Code: Project 1: Operation Selection
#Program:

import math #We will learn more about the math library later. no need to modifiy this line.

BORDER_COUNT = 25
STAR_BORDER = "*" * BORDER_COUNT

print("\n" + STAR_BORDER + "\nPROJECT I\n" + STAR_BORDER)# this line only print a lint of asterisks
# do not delete the following block of instructions
Option = int(input(
    "\nSelect option:\n"
    "(1) Area of figures\n"
    "(2) Units conversion\n"
    "(3) Base conversion\n"
    "(0) Exit\n"))  
#Add the code needed to display the following menu and to complete the task 1a
if Option == 1:
    Area_calculation = int(input(
        "\nSelect option:\n"
        "(1) Area of a SQUARE\n"
        "(2) Area of a RECTANGLE\n"
        "(3) Area of a CIRCLE\n"
        "(4) Area of a TRIANGLE\n"))

    if 1<=Area_calculation<=4:#in [1,2,3,4]: #  ASSUME THE INPUTS ARE INTEGER NUMBERS.
        #IN THIS PHASE YOU DON'T NEED TO VERIFY IF THE INPUT IS AN INTEGER OR A NUMERIC VALUE 
        #Add your code to complete the tasks
        if Area_calculation == 1:
            lattice = float(input('Length? '))
            area = lattice**2
        elif Area_calculation == 2:
            length = float(input('Length? '))
            width = float(input('width? '))
            area = length * width
        elif Area_calculation == 3:
            radius = float(input('Radius? '))
            area = math.pi*(radius**2)
        elif Area_calculation == 4:
            base = float(input('base? '))
            height = float(input('height'))
            area = (1/2)*base*height
        
        
        Y_N = input('Do you want to check how many smaller figures fit in the selected figure? ')
        if Y_N == 'y':
            small_area = float(input("What is the area of the smaller figure?"))
            fitting = area // small_area
            print('The smaller figure fits in the area', fitting, 'amounts')
        elif Y_N == 'n':
            print('The desired area is:', area)
        
    else:
        print("Invalid input")



#elif Option == 2:
#    print("You chose option 2")
#elif Option == 3:
#   print("You chose option 3")
#elif Option == 0:
#   print("Exiting the program...")
#else:
#    print("Invalid option")
