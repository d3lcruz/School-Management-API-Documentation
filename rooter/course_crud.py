from fastapi import APIRouter, HTTPException
from pymongo import ReturnDocument
from model.model import Course
from bson import ObjectId
from db.client import collection_course
from db.schemas.schema_course import list_serial


router = APIRouter(prefix='/course',
                   tags=['course'],
                   responses={404:{"message":"No found"}})

@router.get("/")
async def get_todo():
    course = list_serial(collection_course.find())
    return course

@router.post("/", response_model= Course)
async def agg_course(course:Course):
    course_dict = course.dict(exclude_unset=True)
    
    try:
        result = collection_course.insert_one(course_dict)
        course.course_id = str(result.inserted_id)
    except:
        raise HTTPException(status_code=500, detail="Error inserting student into the database")
    
    return course_dict

@router.get("/{course_id}", response_model= Course)
async def show_id(course_id: str):
    
    try:
        obj_id = ObjectId(course_id)
    except Exception as e:
         raise HTTPException(status_code=400, detail="Invalid student ID format")
     
    read_course = collection_course.find_one({"_id": obj_id})
    if read_course is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    read_course["course_id"] = str(read_course["_id"])
    return Course(**read_course)

@router.put("/{course_id}", response_model= Course)
async def update_course(course_id: str, course: Course):
    course_dict = course.dict(exclude_unset=True)
    
    try:
        obj_id = ObjectId(course_id)
    except Exception as e:
         raise HTTPException(status_code=400, detail="Invalid student ID format")
     
    update_course = collection_course.find_one_and_update({"_id": obj_id}, {"$set": course_dict}, return_document=ReturnDocument.AFTER)
    
    if update_course is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_course["course_id"] = str(update_course["_id"])
    return Course(**update_course)

@router.delete("/{course_id}", response_model= Course)
async def clean_course(course_id:str):
    
    try:
        obj_id = ObjectId(course_id)
    except Exception as e:
         raise HTTPException(status_code=400, detail="Invalid student ID format")
     
    found = collection_course.find_one_and_delete({"_id": obj_id})
    if found is None:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    found["course_id"] = str(found["_id"])
    del found["_id"]
    
    return Course(**found)