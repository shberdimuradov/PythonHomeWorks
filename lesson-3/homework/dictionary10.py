student = {
    "id": 101,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
}

key = "id"  # yoki istalgan kalit

if key in student:
    print((key, student[key]))  # kalit-qiymat juftligini tuple ko'rinishida chiqaradi
else:
    print(f"'{key}' kaliti lug'atda mavjud emas.")