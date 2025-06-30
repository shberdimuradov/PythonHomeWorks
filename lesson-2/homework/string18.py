text = input("Matn kiriting: ")
start_word = input("Qaysi so'z bilan boshlanishi kerak: ")
end_word = input("Qaysi so'z bilan tugashi kerak: ")

if text.startswith(start_word) and text.endswith(end_word):
    print("✅ Matn belgilangan so'z bilan boshlanadi va tugaydi.")
else:
    print("❌ Matn shartlarga mos emas.")