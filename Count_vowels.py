# Count the vowels in the String - Way 1
def countVowel(string):
    count = 0
    vowel='aeiouAEIOU'
    for char in string:
        if char in vowel:
            count+=1
    return count if count else None

count_vowel = countVowel(input("Enter the string:"))
if count_vowel is not None:
    print(f"Count of vowels in the string:{count_vowel}")
else:
    print("No vowels in the given string")

"""
Input: Enter the string: python program
Output: Count of vowels in the string: 3
"""



# Count the vowels in the String - Way 2 (list comprehension)
def countVowel(string):
    vowels='aeiouAEIOU'
    count= len([char for char in string if char in vowels])
    return count if count else None

count_vowel = countVowel(input("Enter the string:"))
if count_vowel is not None:
    print(f"Count of vowels in the string:{count_vowel}")
else:
    print("No vowels in the given string")






# Count the vowels in the String - Way 3 (generator expression)
def countVowel(string):
    vowels='aeiouAEIOU'
    return sum(1 for char in string if char in vowels) or None

count_vowel = countVowel(input("Enter the string:"))
if count_vowel is not None:
    print(f"Count of vowels in the string:{count_vowel}")
else:
    print("No vowels in the given string")





