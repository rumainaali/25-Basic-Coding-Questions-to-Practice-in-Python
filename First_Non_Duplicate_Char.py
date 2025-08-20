# Find the First Non Duplicate Character in the String
def firstNonDuplicateChar(string):
    freq={}
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
            
    for char in string:
        if freq[char]==1:
            return char
    return None
    
unique_char = firstNonDuplicateChar(input("Enter the string:"))
if unique_char:
    print(f"First Non Duplicate Character in the given string: {unique_char}")
else:
    print("No unique character")

"""
Input: Enter the string: swiss
Output:First Non Duplicate Character in the given string: w
"""
