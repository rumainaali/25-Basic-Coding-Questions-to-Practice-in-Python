# Right Angle Triangle - Way 1(Without space inbetween the stars)
def rightAngleTrianglePattern(rows):
    if rows >= 2:
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print("*",end="")
            print()
    else:       
        print("Please provide a number greater than 1 to form right angle triangle pattern")
   
rightAngleTrianglePattern(int(input("Enter number of rows:")))

"""
Input: Enter number of rows: 5
Output:
*
**
***
****
*****
"""


# Right Angle Triangle - Way 2(With space inbetween)
def rightAngleTrianglePattern(rows):
    if rows >= 2:
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    else:       
        print("Please provide a number greater than 1 to form right angle triangle pattern")
   
rightAngleTrianglePattern(int(input("Enter number of rows:")))

"""
Input: Enter number of rows: 5
Output:
*
* *
* * *
* * * *
* * * * *
"""


