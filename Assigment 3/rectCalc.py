print("Enter the length and width of the rectangle A:")
lengthA = float(input("Length: "))
widthA = float(input("Width: "))

print("Enter the length and width of the rectangle B:")
lengthB = float(input("Length: "))        
widthB = float(input("Width: "))

areaA = lengthA * widthA    
areaB = lengthB * widthB

print ("Area of rectangle A:", areaA)
print ("Area of rectangle B:", areaB)

if (areaA > areaB):
    print("Rectangle A has a larger area than Rectangle B.")

elif (areaA < areaB):
    print("Rectangle B has a larger area than Rectangle A.")

else:
    print("Both rectangles have the same area.")

    