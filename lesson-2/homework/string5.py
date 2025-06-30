word = 'Assalomu aleykum'
vowels = 'aeiou'
count = 0

for vow in word.lower():
    if vow in vowels:
        count += 1

print(f"Unli harflar soni: {count} ta")
        
    