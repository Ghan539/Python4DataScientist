# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers 

L = [1,2,3,4,5,6]


a1=[i for i in L if i%2!=0]
print(a1)


a2=[i for i in L if i%2==0]
print(a2)