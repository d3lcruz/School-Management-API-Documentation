def individual_serial(course) -> dict:
    return {
        "id": str (course["course_id"]),
        "title": course["title"],
        "description": course["description"]
    }
    
def list_serial(courses) -> list:
    return[individual_serial(course) for course in courses]