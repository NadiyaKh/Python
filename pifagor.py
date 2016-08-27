# def pifagor (x):
# 	d1= range (1,x+1)
# 	pif_list = []
# 	a = b = c= 1
# 	b
# While (a+b)<c
# 	for i in d1:
# 		c+=1
# 		if in d1:
# 			b+=1
# 			for k in d1:
# 				c+=1
# 				if (a**2 + b**2) = c**:
# 					pif_list.append(a,b,c)
# 					if len(pif_list)=x*3:
# 						break

# 	print (pif_list)

# pifagor(50)

#for c in range (1000)
	#for a in range (1000)
			#for d in range (1000)

# t=[[a, b, c] for c in range(1000) for b in range (c) for a in range(b) if a**2+b**2==c**2]  = list comprehension

# NEW ONE VERSION OF RESOLVING!!!! Необмежений по клькості в результаті


from itertools import count
x = int(input("enter triples count:"))

def triplets(x):
	t=[]
	g=([a, b, c] for c in count() for b in range (c) for a in range(b) if a**2+b**2==c**2) # generator expression

	for  i in range (x):
		t.append(next(g))
	return t


print (triplets(x))


#work code 
# a = b = c =1
# t=[]
# x = int(input("enter triples count:"))

# while len(t)<x:
# 	c+=1
# 	for b in range(1, c):
# 		for a in range (1,b):
# 			if a**2 + b**2 == c**2
# 				t.append([a,b,c])

# print(t)



x = int(input("enter triples count:"))

def triplets(x):
	a = b = c =1
	t=[]
	while len(t)<x:
		c+=1
		for b in range(1, c):
			for a in range (1,b):
				if a**2 + b**2 == c**2
					t.append([a,b,c])
	return t
print(triplets(x))

itertools
collections