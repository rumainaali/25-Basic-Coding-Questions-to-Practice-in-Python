------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Maximum of three numbers - Way 1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def maxThreeNum(n):
    if len(n)==3:
        maximum=n[0]
        if n[1]>maximum:
            maximum=n[1]
        if n[2]>maximum:
            maximum=n[2]
        return maximum
    return None

max_num = maxThreeNum(list(map(int,input("Enter three numbers:").split(" "))))
if max_num is not None:
    print(f"{max_num} is the Maximum number")
else:
    print("Please give only three numbers")


------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Maximum of three numbers - Way 2 (Using max())
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def maxThreeNum(n):
    if len(n)==3:
        return max(n)
    return None

max_num = maxThreeNum(list(map(int,input("Enter three numbers:").split(" "))))
if max_num is not None:
    print(f"{max_num} is the Maximum number")
else:
    print("Please give only three numbers")


"""
Input: Enter three numbers: -1 0 -2
Output: 0 is the Maximum number
"""

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Maximum of three numbers - Way 3 (Using Multiple Variables along with max())
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def maxThreeNum(a,b,c):
    return max(a,b,c)
   

a,b,c = map(int,input("Enter three numbers:").split(" "))
max_num = maxThreeNum(a,b,c)
print(f"{max_num} is the Maximum number")


------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Maximum of three numbers - Way 4 (Using Multiple Variables without max())
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def maxThreeNum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

a,b,c = map(int,input("Enter three numbers:").split(" "))
max_num = maxThreeNum(a,b,c)
print(f"{max_num} is the Maximum number")


------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Maximum of three numbers - Way 5
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def maxThreeNum(n):
    if len(n)==3:
        if n[0]>=n[1] and n[0]>=n[2]:
            return n[0]
        elif n[1]>=n[0] and n[1]>=n[2]:
            return n[1]
        else:
            return n[2]
    return None

max_num = maxThreeNum(list(map(int,input("Enter three numbers:").split(" "))))
if max_num is not None:
    print(f"{max_num} is the Maximum number")
else:
    print("Please give only three numbers")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
