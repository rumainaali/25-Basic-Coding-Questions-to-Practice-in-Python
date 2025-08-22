# Hollow Square Pattern
def hollowSquarePattern(rows):
    if rows>=2:
        for i in range(1,rows+1):
            for j in range(1,rows+1):
                if(i==1 or i==rows or j==1 or j==rows):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    else:
        print("Please enter number greater than 1 to form hollow square")

hollowSquarePattern(int(input("Enter number of rows:")))

"""
Input:4
Output:
* * * *
*     *
*     *
* * * *
"""
    
