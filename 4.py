#Answer 4
def power(a,b):
	if b==1:
		return a
	else:
		return a*power(a,b-1)
a=int(input("Enter number to find power of:"))
b=int(input("Enter power:"))
print(power(a,b))
