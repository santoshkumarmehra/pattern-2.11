n=int(input("enter the no = "))
result="" 
for i in range(1,n+1):
	x=1
	flag=0
	for j in range(1,2*i):
		result=result+str(x)+" "
		if flag==0:
			x=x+1
		else:
			x=x-1
		if x==i:
			flag=1
	result=result+"\n"
print(result)