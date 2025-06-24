nums = [1,2,3,4,5,6,7,8,9,10,11,12]
odd = sum(1 for num in nums if num % 2 == 1)
print("Odd count:", odd)