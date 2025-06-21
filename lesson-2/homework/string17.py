# 17st.

text = input("Matn kiriting: ")

vowels = 'aeiouAEIOU'

for vowel in vowels:
    text = text.replace(vowel, '*')

print("Natija:", text)