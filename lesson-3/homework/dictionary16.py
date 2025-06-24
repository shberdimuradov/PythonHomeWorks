students = {
    "student1": {"name": "Ali", "age": 21, "major": "Math"},
    "student2": {"name": "Laylo", "age": 22, "major": "Biology"}
}

print(any(isinstance(v, dict) for v in students.values()))