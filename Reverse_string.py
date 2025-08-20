# Reverse the string - Way 1(Using Slicing)
def revStr(strings):
    return strings[::-1]
    
reversed_string = revStr(input("Enter the String:"))
print(reversed_string)

"""
Sample Input and Ouput

Input:Enter the String: 1 2 3 hello
Output:
  olleh 3 2 1
"""

# Reverse the string - Way 2(Using For Loop)
def revStr(strings):
    rev_str = ""
    for char in strings:
        rev_str = char + rev_str
    return rev_str    
    
reversed_string = revStr(input("Enter the string:"))
print(reversed_string)

"""
Sample Input and Ouput

Input:Enter the String: 1 2 3 hello -1
Output:
  1- olleh 3 2 1
"""
