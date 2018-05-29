#Answer 5
def factorial(num):
	if num==1:
		return 1
	else:
		return num*factorial(num-1)
num=int(input("Enter number to find factorial of:"))
a=factorial(num)
dict={}
dict[num]=a
print(dict)
