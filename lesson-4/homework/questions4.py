# How would you implement a nested for loop system? Provide an example.
# A nested for loop is a loop inside another loop. It’s typically used when dealing with 
# multi-dimensional data structures like matrices or grids.
rows = 3
cols = 2

for i in range(rows):
    for j in range(cols):
        print(f"Cell ({i}, {j})")


# Output:
# scss
# Копировать
# Редактировать
# Cell (0, 0)
# Cell (0, 1)
# Cell (1, 0)
# Cell (1, 1)
# Cell (2, 0)
# Cell (2, 1)