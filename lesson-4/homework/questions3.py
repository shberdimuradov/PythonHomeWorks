# What is the difference between a for loop and a while loop in Python?
# A for loop is used when you know in advance how many times you want to iterate.

# A while loop is used when you want to loop until a condition becomes false, regardless of how many iterations it takes.

# ✅ Example:

# For loop: iterate 5 times (known range)
for i in range(5):
    print(i)

# While loop: iterate until condition is no longer true
i = 0
while i < 5:
    print(i)
    i += 1
