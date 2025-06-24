student = {
    "id": 20,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
}

new = {value: key for key,value in student.items()}

print(new)