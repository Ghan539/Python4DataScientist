# Write a program to replace an item with a different item if found in the list 
L = [1,2,3,4,5,3]
# replace 3 with 300

for i in range(len(L)):
    if L[i] ==3:
        L[i]=300
         
print(L)      



# 2nd method 
ans=[300 if i==3 else i for i in L  ]
print(ans)