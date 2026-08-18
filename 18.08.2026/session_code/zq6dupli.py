# Write a program to remove duplicate items from a list

L = [1,2,1,2,3,4,5,3,4]

ans=[]

for i in L:
    if i not in ans :
        ans.append(i)

print(ans)            




