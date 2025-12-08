# Common elements in two lists - Way 1
def findComEle(list1,list2):
    com_ele = []
    for i in list1:
        if i in list2:
            if i not in com_ele:
                com_ele.append(i)
    return com_ele if com_ele else None

result = findComEle(list(map(int,input("Enter the numbers for list 1:").split())),list(map(int,input("Enter the numbers for list 2:").split())))
if result is not None:
    print("Common elements in two lists:",result)
else:
    print("No common elements")

"""
Input:Enter the numbers for list 1: 1 2 3 1
Enter the numbers for list 2: 2 4 6 1
Output: Common elements in two lists: [1,2]
"""

# Common elements in two lists - Way 2(Using set())
def findComEle(list1,list2):
    com_ele = list(set(list1)&set(list2))
    return com_ele if com_ele else None

result = findComEle(list(map(int,input("Enter the numbers for list 1:").split())),list(map(int,input("Enter the numbers for list 2:").split())))
if result is not None:
    print("Common elements in two lists:",result)
else:
    print("No common elements")

"""
Input:Enter the numbers for list 1: 1 2 3 1
Enter the numbers for list 2: 2 2 4 3
Output: Common elements in two lists: [2,3]
"""


# Common elements in two lists - Way 3(Using list comprehension and set())
def findComEle(list1,list2):
    visited = set()
    com_ele = [i for i in list1 if i in list2 and (i not in visited and not visited.add(i))]
    return com_ele if com_ele else None

result = findComEle(list(map(int,input("Enter the numbers for list 1:").split())),list(map(int,input("Enter the numbers for list 2:").split())))
if result is not None:
    print("Common elements in two lists:",result)
else:
    print("No common elements")
"""
Input:Enter the numbers for list 1: 1 2 2 3
Enter the numbers for list 2: 2 2 1
Output: Common elements in two lists: [1,2]
"""
