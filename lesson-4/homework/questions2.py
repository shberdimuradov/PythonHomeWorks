#  1. What is the difference between the continue and break statements in Python?
# The break statement immediately exits the loop, regardless of the loop condition.

# The continue statement skips the current iteration and proceeds with the next one.

# ✅ Example:
for i in range(5):
    if i == 3:
        break       # Loop stops completely when i == 3
    print(i)

# Output: 0, 1, 2

for i in range(5):
    if i == 3:
        continue    # Skip i == 3, but loop continues
    print(i)

# Output: 0, 1, 2, 4

