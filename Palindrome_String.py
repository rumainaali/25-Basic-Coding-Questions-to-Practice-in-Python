# Check if a String is a Palindrome - Way 1
def isPalindromeOrNot(string):
    cleaned=""
    for char in string:
        if char.isalnum():
            cleaned+=char.lower()
    
    if cleaned==cleaned[::-1]:
        return "The given string is Palindrome"
    else:
        return "The given string is not a Palindrome"

print(isPalindromeOrNot(input("Enter the string:")))

"""
Input: Enter the String: Mam
Output:The given string is Palindrome

Input: Enter the String: A man, a plan, a canal, Panama!
Output:The given string is Palindrome
"""



# Check if a String is a Palindrome - Way 2(Using re(Regular Expression))
import re
def isPalindromeOrNot(string):
    cleaned = re.sub(r'[^a-zA-Z0-9]','',string).lower()
    if cleaned==cleaned[::-1]:
        return "The given string is Palindrome"
    else:
        return "The given string is not a Palindrome"

print(isPalindromeOrNot(input("Enter the String:")))

