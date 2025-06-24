numbers = (1, 2, 3, 4, 5, 6, 7)
repeat = 3
temp_list = []

for x in numbers:
    temp_list.extend([x] * repeat)

new_tuple = tuple(temp_list)

print(new_tuple)
