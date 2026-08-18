# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

ans=[i for i in my_fruits if i in basket and i.startswith('a') ]
print(ans)


ans=[]

for i in my_fruits:
    if i in basket and  i.startswith('a'):
       ans.append(i)
print(ans)        