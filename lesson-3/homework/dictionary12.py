student = {
    "id": 20,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
}

target_value = 20
count = sum(1 for value in student.values() if value == target_value)
print(count)