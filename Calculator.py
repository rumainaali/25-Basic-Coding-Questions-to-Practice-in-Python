# Calculator
def add(a,b):
    return a + b

def sub(a,b):
    return a - b
    
def mul(a,b):
    return a * b
    
def div(a,b):
    return a/b if b!=0 else "Cannot be divided by zero"

a,b = map(int,input("Enter two numbers:").split())
operations = int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter operation(1/2/3/4):"))

if operations == 1:
    print(add(a,b))
elif operations == 2:
    print(sub(a,b))
elif operations == 3:
    print(mul(a,b))
elif operations == 4:
    print(div(a,b))
else:
    print("Please enter valid number")


"""
Input:Enter two numbers: 1 2
1.Add
2.Subtract
3.Multiply
4.Divide
Enter operation(1/2/3/4):2
Output: -1

Input:Enter two numbers: 9 0
1.Add
2.Subtract
3.Multiply
4.Divide
Enter operation(1/2/3/4):4
Output: Cannot be divided by zero
"""
    
    
    
    
    
    
    
    
    
