from fastapi import FastAPI, Path

from pydantic import BaseModel

from typing import Optional

# import data as students

import json

app = FastAPI()


with open('data.json', 'r') as f:
    students = json.load(f)

class Student(BaseModel):
    name: str
    age: int
    year: str



@app.get("/")

def index():
    return {"message": "hii"}


@app.get("/student-data/")

def getStudentData():
    return students

@app.get("/student-data/{id}")

def getStudentData(id:str):
    return students[id]


@app.get("/student-name")

def getStudentData(name: str):
    for id in students:
        if students[id]["name"] == name:
            return students[id]
        
    return {"Error" : "not found"}




@app.post("/create-student/{id}")

def createStudent(id:str, st1: Student):
    if id in students:
        return {"Error" : "Already exists"}
    
    students[id] = st1.dict()
    
    with open('data.json', 'w') as f:
        json.dump(students, f)

    return students[id]


@app.put("/update-student/{id}")

def updateStudent(id:str, st1: Student):
    if id not in students:
        return {"Error" : "Not found"}
    
    students[id].update(st1)

    with open('data.json', 'w') as f:
        json.dump(students, f)

    return students[id]


@app.delete("/delete-student/{id}")

def deleteStudent(id:str):
    if id not in students:
        return {"Error" : "Not found"}
    
    students.pop(id)

    with open('data.json', 'w') as f:
        json.dump(students, f)

    return {"Success" : "user {id} successfully deleted"}