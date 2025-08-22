# Find the Factorial of a Number - Way 1
def factorialOfNumber(n):
    if n<0:
        return None
    if n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact

factorial_number = factorialOfNumber(int(input("Enter the number:")))
if factorial_number is not None:
    print(f"Factorial of the given number is:{factorial_number}")
else:
    print("Please enter number greater than -1")
"""
Input: Enter the number: 5
Output:Factorial of the given number is:120
"""


# Find the Factorial of a Number - Way 2(Using Recursive Function)
def factorialOfNumber(n):
    if n<0:
        return None
    if n==0:
        return 1
    else:
        return n*factorialOfNumber(n-1)

factorial_number = factorialOfNumber(int(input("Enter the number:")))
if factorial_number is not None:
    print(f"Factorial of the given number is:{factorial_number}")
else:
    print("Please enter number greater than -1")


