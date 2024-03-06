a=[]
for i in range(1,3):
	x=int(input("Enter: "))
	a.append(x)
	print(a)
b=[]
for i in range(1,3):
	y=int(input("Enter: "))
	b.append(y)
	print(b)
dot_product=sum(x*y for x,y in zip(a,b))
print("dot product",dot_product)
