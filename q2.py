# i=int(input("Enter no. : "))
i=4
x=i/2
l=[]
for n in range(1,i+1):
	a=n
	if a<=x:	
		print(a)
		l.append([[]])
	n=n*n

print(l)