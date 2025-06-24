a = [1, 2, 3, 4, 10, 9, 7, 8, 6, 5]
repeat_count = 2

result = [item for item in a for _ in range(repeat_count)]

print(result)
