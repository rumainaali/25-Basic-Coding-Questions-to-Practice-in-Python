# Perfect Square (Checks whether a number is a perfect square)
def perfectSquare(num):
    if num>0:
        return num if (num**0.5)**2 == num else False
    else:
        return False

result = perfectSquare(int(input("Enter the number:")))
if result:
    print(f"{result} is a Perfect square")
else:
    print("Not a Perfect square")

"""
Input:Enter the number: 16
Output:16 is a Perfect square
"""

