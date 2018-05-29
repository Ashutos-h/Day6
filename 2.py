#Answer 2
def perfect(num):
	sum=0
	for i in range(1,num):
		if num%i==0:
			sum+=i
	if sum==num:
		print(num)
print("List of perfect numbers:")		
for i in range(1,1001):
	perfect(i)
	
	
	