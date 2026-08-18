ls=[12,13,14,15,16]

sc=5

ls2=[i**2 for i in ls]
print(ls2)


# print all numbers 1-100 divisible by 5
ls2=[i for i in range(1,100) if i%5==0]
print(ls2)

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

ls=[i for i in languages if i.startswith("p")]

print(ls)

