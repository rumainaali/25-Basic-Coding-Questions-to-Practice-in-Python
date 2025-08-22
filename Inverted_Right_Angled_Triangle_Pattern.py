# Inverted Right Angle Triangle
def invertedRightAngleTrianglePattern(rows):
    if rows >= 2:
        for i in range(rows,0,-1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    else:       
        print("Please provide a number greater than 1 to form inverted right angle triangle pattern")
   
invertedRightAngleTrianglePattern(int(input("Enter number of rows:")))

"""
Input: Enter number of rows: 5
Output:
* * * * *
* * * *
* * *
* *
*
"""
