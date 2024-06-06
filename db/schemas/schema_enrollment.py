def individual_serial(enrollment) -> dict:
    return {
        "id": str (enrollment["enrollment_id"]),
        "student_id": enrollment["student_id"],
        "course_id": enrollment["course_id"]
        #"student_id": str (student["student_id"])
    }
    
def list_serial(enrollments) -> list:
    return[individual_serial(enrollment) for enrollment in enrollments]