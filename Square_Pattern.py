# Square Pattern
def squarePattern(rows):
    if rows >= 2:
        for i in range(1,rows+1):
            for j in range(1,rows+1):
                print("*",end="")
            print()
    else:       
        print("Please provide a number greater than 1 to form square")
    
squarePattern(int(input("Enter number of rows:")))

"""
Input: Enter number of rows: 3
Output:
***
***
***

"""
