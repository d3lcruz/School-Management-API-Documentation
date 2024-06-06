def individual_serial(student) -> dict:
    return {
        "id": str (student["student_id"]),
        "age": student["age"],
        "name": student["name"]
    }
    
def list_serial(students) -> list:
    return[individual_serial(student) for student in students]
