from fastapi import APIRouter, HTTPException
from pymongo import ReturnDocument
from model.model import Enrollment
from bson import ObjectId
from db.client import collection_enrollment
from db.schemas.schema_enrollment import list_serial

router = APIRouter(prefix='/enrollment',
                   tags=['enrollment'],
                   responses={404:{"message":"No found"}})

@router.post("/", response_model= Enrollment)
async def agg_enrollment(enrolment: Enrollment):
    enrolment_dict = enrolment.dict(exclude_unset=True)
    
    try:
        enrolment_agg = collection_enrollment.insert_one(enrolment_dict)
        enrolment.enrollment_id = str(enrolment_agg.inserted_id)
    except:
        raise HTTPException(status_code=500, detail="Error inserting student into the database")

    return enrolment_dict

@router.get("/{enrollment_id}", response_model=Enrollment)
async def read_enrollment(enrollment_id: str):
    
    try:
        obj_id = ObjectId(enrollment_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    get_enrollment = collection_enrollment.find_one({"_id": obj_id})
    if get_enrollment is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    get_enrollment["enrollment_id"] = str(get_enrollment["_id"])
    return Enrollment(**get_enrollment)

@router.put("/{enrollment_id}", response_model=Enrollment)
async def update_enroll(enrollment_id:str, enrollment:Enrollment):
    enrollment_dict = enrollment.dict(exclude_unset=True)
    
    try:
        obj_id = ObjectId(enrollment_id)
    except Exception as e:
         raise HTTPException(status_code=400, detail="Invalid student ID format")
     
    new_enroll = collection_enrollment.find_one_and_update({"_id": obj_id}, {"$set": enrollment_dict}, return_document=ReturnDocument.AFTER)
    
    if new_enroll is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_enroll["enrollment_id"] = str(new_enroll["_id"])
    return Enrollment(**new_enroll)   

@router.delete("/{enrollment_id}", response_model=Enrollment)
async def clean_enroll(enrollment_id:str):
    
    try:
        obj_id = ObjectId(enrollment_id)
    except Exception as e:
         raise HTTPException(status_code=400, detail="Invalid student ID format")
     
    found = collection_enrollment.find_one_and_delete({"_id": obj_id})
    if found is None:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    found["enrollment_id"] = str(found["_id"])
    del found["_id"]
    
    return Enrollment(**found)