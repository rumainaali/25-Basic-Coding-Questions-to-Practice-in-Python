# Sort the list in descending order - Way 1(Using temporary variable)
arr = list(map(int,input("Enter the number:").split()))
temp=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Sorted List in Descending order :",arr)

"""
Input: Enter the number: 9 2 1 4
Output: Sorted List in Descending order:[9,4,2,1]
"""



# Sort the list in descending order - Way 2(Without using temp variable)
arr = list(map(int,input("Enter the number:").split()))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
print("Sorted List in Descending order :",arr)

"""
Input: Enter the number: 8 6 9 0
Output: Sorted List in Descending order:[9,8,6,0]
"""
