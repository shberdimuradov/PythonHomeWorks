a = (1,2,3,2,4,8,2,6)
target = 2

temp = list(a)
temp.remove(target)
b = tuple(temp)

print(b)