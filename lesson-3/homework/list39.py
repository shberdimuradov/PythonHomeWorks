a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
group_size = 3

result = [a[i:i+group_size] for i in range(0, len(a), group_size)]

print(result)
