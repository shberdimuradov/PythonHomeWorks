from collections import Counter


list1 = [1, 1, 2]
list2 = [2, 3, 4]

c1 = Counter(list1)
c2 = Counter(list2)


only_in_1 = c1 - c2

only_in_2 = c2 - c1


result = list(only_in_1.elements()) + list(only_in_2.elements())
print(result)  

print('===================================================================================')

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)

print('===================================================================================')

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(result)