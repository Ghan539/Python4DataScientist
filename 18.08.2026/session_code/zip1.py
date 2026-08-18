# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]


print(list(zip(L1,L2)))

ans=[i+j for i,j in zip(L1,L2)]
print(ans)

ans2=[]

for i,j in zip(L1,L2):
    ans2.append(i+j)
print(ans2)        