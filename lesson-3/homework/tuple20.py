a = (1, 2, 3, 4, 5, 6, 7)
size = 3
subtuples = tuple(a[i:i+size] for i in range(0, len(a), size))
print(subtuples)