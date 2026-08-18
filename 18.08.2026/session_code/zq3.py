# How to take list as input from user

ls=[]

while(True):
    inp=input("Enter items : ")
    
    if inp=="x":
      break 
        
    ls.append(inp)
       
print(ls)    
   