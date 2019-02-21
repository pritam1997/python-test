n = int (input("how much string you want to enter : "))
s2=''
l=[]
for x in range(1,n+1):
	s=input("Enter string : ")
	l.append(s)
l.sort()
print(l)
