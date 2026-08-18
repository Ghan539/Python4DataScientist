# Write a program that can convert a 2D list to 1D list

L = [[1, 2], [3, 4], [5, 6]]

ans=[]
for i in L :
    for j in i:
        ans.append(j)
       
print(ans)        
        