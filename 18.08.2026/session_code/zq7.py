# Write a program to check if a list is in ascending order or not

ls=[88,99,33,34,65,43,55,34,22]

for i in range(0,len(ls)-1):
    if ls[i]>ls[i+1]:  
        print("not asscending")
        break;

else:
   print("asscending")
        
        
    