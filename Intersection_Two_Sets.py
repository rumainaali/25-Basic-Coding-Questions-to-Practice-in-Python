# Intersection of two sets
def intersectionOfSets(set1,set2):
    inter_sets = set(set1 & set2)
    return inter_sets if inter_sets else None

result = intersectionOfSets(set(map(int,input("Enter the numbers for set 1:").split())),set(map(int,input("Enter the numbers for set 2:").split())))
if result is not None:
    print("Intersection of two sets:",result)
else:
    print("No common elements")

"""
Input: Enter the numbers for set 1:4 5 6 7 2
Enter the numbers for set 2:1 2 3 3 4
Output:Intersection of two sets:{2,4}
"""
