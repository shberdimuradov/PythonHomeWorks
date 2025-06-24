student = {
    "id": 10,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
}


sorted_dict = dict(sorted(student.items(), key=lambda item: str(item[1])))
print(sorted_dict)