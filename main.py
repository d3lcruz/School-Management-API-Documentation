from fastapi import FastAPI
#from motor.motor_asyncio import AsyncIOMotorClient
from rooter import student_crud, course_crud, enrollment_crud

app = FastAPI()
app.include_router(student_crud.rooter)
app.include_router(course_crud.router)
app.include_router(enrollment_crud.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Management API"}


# uvicorn main:app --reload
