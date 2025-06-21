# 16st.
import string
s = input("how much for the maple syrup? $20.99? That's ricidulous!!!")
for char in string.punctuation:
    s = s.replace(char, ' ')
