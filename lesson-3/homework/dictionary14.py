student = {
    "id": 20,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
}
target_value = 20

new = [key for key, value in student.items() if value==target_value]

print(new)