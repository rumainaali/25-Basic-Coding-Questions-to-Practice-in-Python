# Perfect Square
def perfectSquare(num):
    i=1
    print("Perfect square numbers are:",end=" ")
    while i*i <= num:
        print(i*i,end=" ")
        i+=1

perfectSquare(int(input("Enter the number:")))

"""
Input: Enter the number:100
Output: Perfect square numbers are: 1 4 9 16 25 36 49 64 81 100
"""
