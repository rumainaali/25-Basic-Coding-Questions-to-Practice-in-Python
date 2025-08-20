# Concatenate strings using join
def concatenateStrings(string):
    return ''.join(string)

concatenated_string = concatenateStrings(list(map(str,input("Enter the strings: ").split(" "))))
print(concatenated_string)

"""
Input:
    Enter the strings: Rumaina is learning python
Output:
    Rumainaislearningpython
"""
