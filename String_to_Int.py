# Convert String to Integer
def strToInt(string):
    if string.startswith('-') and string[1:].isdigit():
        return int(string)
    elif string.isdigit():
        return int(string)
    return None

integer = strToInt(input("Enter the string:"))
if integer is not None:
    print(integer)
else:
    print("Please enter integer only")


"""
Input:-2
Output:-2
"""
