from pydantic import BaseModel
from typing import Optional, List

class Student(BaseModel):
    name:str
    age:int
    student_id: Optional[str] = None
    
class Course(BaseModel):
    title:str
    description:str
    course_id: Optional[str] = None

class Enrollment(BaseModel):
    student_id: str
    course_id: str
    enrollment_id: Optional[str] = None