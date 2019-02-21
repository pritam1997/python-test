n = int ( input ("HOW MUCH NO. YOU WNT TO ENTER. : "))
l=[]
for x in range(1,n+1):
	i = int ( input ("Enter no. : "))
	s=f'{i}'
	l.append(s)
print(l)
t=tuple(l)
print(t)