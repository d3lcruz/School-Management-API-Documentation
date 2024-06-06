School Management API Documentation
Overview

The School Management API is designed to manage a school system, including students, courses, and enrollments. This API is built using FastAPI and MongoDB.
General Information

    Base URL: The base URL for accessing the API is http://localhost:8000.
    Welcome Message: A welcome message can be retrieved from the root endpoint (/).

Endpoints
Students

    Get All Students
        Method: GET
        Endpoint: /students/
        Description: Fetches a list of all students in the database.

    Create a Student
        Method: POST
        Endpoint: /students/
        Request Body: JSON object with name (string) and age (integer).
        Description: Adds a new student to the database and returns the created student object.

    Get Student by ID
        Method: GET
        Endpoint: /students/{student_id}
        Path Parameter: student_id (string) - The ID of the student.
        Description: Retrieves a student by their ID.

    Update Student
        Method: PUT
        Endpoint: /students/{student_id}
        Path Parameter: student_id (string) - The ID of the student.
        Request Body: JSON object with fields to update (e.g., name, age).
        Description: Updates a student’s information and returns the updated student object.

    Delete Student
        Method: DELETE
        Endpoint: /students/{student_id}
        Path Parameter: student_id (string) - The ID of the student.
        Description: Deletes a student from the database and returns the deleted student object.

Courses

    Get All Courses
        Method: GET
        Endpoint: /course/
        Description: Fetches a list of all courses in the database.

    Create a Course
        Method: POST
        Endpoint: /course/
        Request Body: JSON object with title (string) and description (string).
        Description: Adds a new course to the database and returns the created course object.

    Get Course by ID
        Method: GET
        Endpoint: /course/{course_id}
        Path Parameter: course_id (string) - The ID of the course.
        Description: Retrieves a course by its ID.

    Update Course
        Method: PUT
        Endpoint: /course/{course_id}
        Path Parameter: course_id (string) - The ID of the course.
        Request Body: JSON object with fields to update (e.g., title, description).
        Description: Updates a course’s information and returns the updated course object.

    Delete Course
        Method: DELETE
        Endpoint: /course/{course_id}
        Path Parameter: course_id (string) - The ID of the course.
        Description: Deletes a course from the database and returns the deleted course object.

Enrollments

    Create an Enrollment
        Method: POST
        Endpoint: /enrollment/
        Request Body: JSON object with student_id (string) and course_id (string).
        Description: Adds a new enrollment to the database and returns the created enrollment object.

    Get Enrollment by ID
        Method: GET
        Endpoint: /enrollment/{enrollment_id}
        Path Parameter: enrollment_id (string) - The ID of the enrollment.
        Description: Retrieves an enrollment by its ID.

    Update Enrollment
        Method: PUT
        Endpoint: /enrollment/{enrollment_id}
        Path Parameter: enrollment_id (string) - The ID of the enrollment.
        Request Body: JSON object with fields to update (e.g., student_id, course_id).
        Description: Updates an enrollment’s information and returns the updated enrollment object.

    Delete Enrollment
        Method: DELETE
        Endpoint: /enrollment/{enrollment_id}
        Path Parameter: enrollment_id (string) - The ID of the enrollment.
        Description: Deletes an enrollment from the database and returns the deleted enrollment object.

Models
Student

    Fields:
        name (string): The name of the student.
        age (integer): The age of the student.
        student_id (optional string): The unique ID of the student.

Course

    Fields:
        title (string): The title of the course.
        description (string): The description of the course.
        course_id (optional string): The unique ID of the course.

Enrollment

    Fields:
        student_id (string): The ID of the student.
        course_id (string): The ID of the course.
        enrollment_id (optional string): The unique ID of the enrollment.

Database
Collections

    Students Collection: Stores student documents.
    Courses Collection: Stores course documents.
    Enrollments Collection: Stores enrollment documents.

Schemas

    Student Schema: Defines the structure of student documents.
    Course Schema: Defines the structure of course documents.
    Enrollment Schema: Defines the structure of enrollment documents.

This documentation provides an overview of the API, describes each endpoint, and details the data models and database schema used in the application.
