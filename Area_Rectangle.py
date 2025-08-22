# To calculate the Area of Rectangle
def areaRectangle(length,breath):
    if length<=0 or breath<=0:
        return "Length and breath must be greater than 0" 
    elif length == breath:
        return "Length and breath cannot be same values"
    else:
        return f"Area of the Rectangle:{length*breath:.2f}"

values = list(map(float, input("Enter the length and breath of rectangle: ").split()))
if len(values)<2:
    print("Please enter 2 values")
else:
    length,breath=values
    print(areaRectangle(length,breath))

  
"""
Input: Enter the length and breath of rectangle: 10 7
Output: Area of the Rectangle: 70.00
"""
