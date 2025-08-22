# Remove Duplicate Elements from list
def removeDupInList(user_input):
    output = []
    for i in user_input:
        if i not in output:
            output.append(i)
    return output

remove_duplicate = removeDupInList(input("Enter the list:").split())
print(f"After Removing Duplicates: {remove_duplicate}")

"""
Input: Enter the list: 1 1 2 3
Output: After Removing Duplicates: [1,2,3]

Input: Enter the list: a b a aa c
Output: After Removing Duplicates: ['a','b','aa','c']
"""
