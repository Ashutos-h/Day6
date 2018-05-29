#Answer 1
def area(rad):
	area_s=4*3.142*rad*rad
	return area_s
radius=int(input("Enter radius of sphere:"))
print("Area of sphere:",area(radius))