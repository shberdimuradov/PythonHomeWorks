txt = "salomdunhjkhjkhjkhjkhyo"  # bu misol o‘rnida

result = ""
i = 0

while i < len(txt):
    result += txt[i]

    # 1. Har 3-belgidan keyin _
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        result += "_"

    # 2. Agar unli harf bo‘lsa yoki undan oldin _ bo‘lsa
    if txt[i] in "aeiou" or (i > 0 and txt[i - 1] == "_"):
        # Keyingi belgi mavjud bo‘lsa
        if i + 1 < len(txt):
            result += txt[i + 1] + "_"
            i += 1  # qo‘shimcha belgini o‘tkazdik
    i += 1

print(result)
