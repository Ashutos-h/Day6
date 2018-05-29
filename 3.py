#Answer 3
def multiplication(num,k,list):
	if k==1: 
		list.insert(0,num)
	else:
		list.insert(0,(num*k))
		multiplication(num,k-1,list)
list=[]
multiplication(12,10,list)
for i in list:
	print(i)
