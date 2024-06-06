from fastapi import APIRouter, HTTPException
from pymongo import ReturnDocument
from model.model import Student
from bson import ObjectId
from db.client import collection
from db.schemas.schema_student import list_serial

rooter = APIRouter(prefix='/students',
                   tags=['students'],
                   responses={404:{"message":"No found"}})

@rooter.get("/")
async def get_todo():
    student = list_serial(collection.find())
    return student

@rooter.post("/", response_model=Student)
async def create_student(student: Student):   
    student_dict = student.dict(exclude_unset=True)
    
    try: 
        result = collection.insert_one(student_dict)
        student.student_id = str(result.inserted_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error inserting student into the database") 
    
    return student_dict

@rooter.get("/{student_id}", response_model=Student)
async def read_student(student_id: str):
    
    try:
        obj_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid student ID format")

    student = collection.find_one({"_id": obj_id})
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    student["student_id"] = str(student["_id"])
    return Student(**student)

@rooter.put("/{student_id}", response_model=Student)
async def update_student(student_id: str, student: Student):
    student_update = student.dict(exclude_unset=True)
    
    try:
        obj_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    updated_student = collection.find_one_and_update(
        {"_id": obj_id},
        {"$set": student_update},
        return_document=ReturnDocument.AFTER
    )
    
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    updated_student["student_id"] = str(updated_student["_id"])
    return Student(**updated_student)

@rooter.delete("/{student_id}", response_model=Student)
async def clean_student(student_id: str):
    
    try:
        obj_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    found = collection.find_one_and_delete({"_id": obj_id})
    if found is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    found["student_id"] = str(found["_id"])
    del found["_id"]
    
    return Student(**found)
    


