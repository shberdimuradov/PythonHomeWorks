nums = [1,2,3,4,5,6,7,8,9,10,11,12]

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1 
    else:
        odd += 1
print("Even count:", even)
print("Odd count:", odd)