a = (1, 2, 3, 4, 5, 4, 3, 2, 1)
seen = set()
unique = []

for x in a:
    if x not in seen:
        seen.add(x)
        unique.append(x)

b = tuple(unique)
print(b)