student = {
    "id": 10,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
}

sorted_dict = {key: student[key] for key in sorted(student.keys())}
print(sorted_dict)