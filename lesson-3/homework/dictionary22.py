student = {
    "id": 10,
    "first_name": "Ali",
    "last_name": "Karimov",
    "age": 20,
    "score": 25,
}

filtered_dict = {k: v for k, v in student.items() if isinstance(v, int) and v > 20}

print(filtered_dict)