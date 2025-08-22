# Merge Two Dictionaries - Way 1(Dictionary Unpacking)
def mergeDicts(dict1,dict2):
    merged_dict = {**dict1,**dict2}
    return merged_dict
    

def getDict():
    dictionary = {}
    n = int(input("Enter how many key-value pairs do you want:"))
    for i in range(n):
        key = input(f"Enter the key {i+1}:")
        value = input(f"Enter the value for {key}:")
    
        dictionary[key]=value
    return dictionary
dict1 = getDict()
dict2 = getDict()
merged = mergeDicts(dict1,dict2)
print(f"After Merging 2 Dictionaries: {merged}")

"""
Input:
Enter how many key-value pairs do you want:1
Enter the key 1:a
Enter the value for a:1
Enter how many key-value pairs do you want:2
Enter the key 1:b
Enter the value for b:2
Enter the key 2:c
Enter the value for c:3

Output:
After Merging 2 Dictionaries: {'a': '1', 'b': '2', 'c': '3'}
"""


# Merge Two Dictionaries - Way 2(Using copy() and update())
def mergeDicts(dict1,dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def getDict():
    dictionary = {}
    n = int(input("Enter how many key-value pairs do you want:"))
    for i in range(n):
        key = input(f"Enter the key {i+1}:")
        value = input(f"Enter the value for {key}:")
    
        dictionary[key]=value
    return dictionary
dict1 = getDict()
dict2 = getDict()
merged = mergeDicts(dict1,dict2)
print(f"After Merging 2 Dictionaries: {merged}")


"""
Input:
Enter how many key-value pairs do you want:2
Enter the key 1:a
Enter the value for a:1
Enter the key 2:b
Enter the value for b:2
Enter how many key-value pairs do you want:2
Enter the key 1:b
Enter the value for b:3
Enter the key 2:c
Enter the value for c:4

Output:
After Merging 2 Dictionaries: {'a': '1', 'b': '3', 'c': '4'}
"""
