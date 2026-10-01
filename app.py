from http.client import HTTPException
from fastapi import status

from fastapi import FastAPI
from students import get_all_students, get_student_by_id, calculate_student_status
from pydantic import BaseModel

from students import(
    students,
    get_all_students,
    get_student_by_id,
    calculate_student_status
)



app = FastAPI(
    title="Student Performance API",
    description="API for managing student performance",
    version="1.0.0"
)

#GET

@app.get("/") # / Root endpoint #decorator 
def home(name: str):
    return {
        "message": f"{name},Student Performance API is running"
    }

@app.get("/students")
def get_students():
    return get_all_students()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = get_student_by_id(student_id)

    if student is None:
        return {
            "message": "Student not found"
        }

    return student


@app.get("/students/{student_id}/status")
def get_student_status(student_id: int):
    student = get_student_by_id(student_id)

    if student is None:
        return {
            "message": "Student not found"
        }

    status = calculate_student_status(student)

    return {
        "student_id": student["id"],
        "name": student["name"],
        "attendance": student["attendance"],
        "marks": student["marks"],
        "status": status
    }

#POST
class Student(BaseModel):  #Inheri
    id: int
    name: str
    course: str
    attendance: float
    marks: float


@app.get("/")
def home():
    return {
        "message": "Student Performance API is running"
    }


@app.get("/students")
def get_students():
    return get_all_students()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = get_student_by_id(student_id)

    if student is None:
        return {
            "message": "Student not found"
        }

    return student


@app.get("/students/{student_id}/status")
def get_student_status(student_id: int):
    student = get_student_by_id(student_id)

    if student is None:
        return {
            "message": "Student not found"
        }

    status = calculate_student_status(student)

    return {
        "student_id": student["id"],
        "name": student["name"],
        "attendance": student["attendance"],
        "marks": student["marks"],
        "status": status
    }


@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_student(student:Student):
    if get_student_by_id(student.id) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            details=f"Student with ID {student.id} already exists"
        )
    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }

#DELETE

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    student = get_student_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details=f"Student with ID {student_id} not found"
        )
    students.remove(student)
    return None

#500 error

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    student = get_student_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detls=f"Student with ID {student_id} not found"
        )
    students.remove(student)
    return None

