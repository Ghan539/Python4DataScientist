ls=[10,20,304,5,67,878,98]

ls[0:3]=[100,200,300,400]

print(ls)

ls=[10,20,304,5,67,878,98]
ls[7::]=[122,324,45,767,879]
print(ls)

del ls[-1]
print(ls)

ls.remove(304)
print(ls)

ls.pop()
print(ls)

