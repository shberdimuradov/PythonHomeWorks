a = (1,2,3,2,4,8,2,6)
target = 2

indexes = [index for index, element in enumerate(a) if target==element ]
print(f'Indexes of elements: {indexes}')
    