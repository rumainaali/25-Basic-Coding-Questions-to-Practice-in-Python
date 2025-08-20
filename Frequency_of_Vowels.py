# Count frequency of vowels in a string
def countVowel(string):
    count = {}
    vowel='aeiouAEIOU'
    for char in string:
        if char in vowel:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
    return count if count else None

count_vowel = countVowel(input("Enter the string:"))
if count_vowel is not None:
    print(f"Count of each vowels in the string:{count_vowel}")
else:
    print("No vowels in the given string")

"""
Input: Enter the string:python
Output: Count of each vowels in the string:{'o':1}
"""
