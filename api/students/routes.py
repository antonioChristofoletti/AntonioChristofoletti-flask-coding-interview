from http.client import HTTPException
from typing import Optional

from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field
from sqlalchemy import select

from api.students.models import Students
from database import db

students_app = APIBlueprint("student_app", __name__)


class StudentSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    user_id: int = Field(gt=0)

    class Config:
        orm_mode = True


class StudentList(BaseModel):
    students: list[StudentSchema]


@students_app.get("/students", responses={"200": StudentList})
def get_list():
    with db.session() as session:
        students_query = session.execute(select(Students)).scalars().all()
        students_list = [
            StudentSchema.from_orm(student).dict() for student in students_query
        ]
        return {"users": students_list}


@students_app.get("/students/{student_id}", responses={"200": StudentSchema})
def get_by_id(student_id: int):
    with db.session() as session:
        student = session.query(Students).filter_by(id=student_id).first()

        if student is None:
            raise HTTPException(
                status_code=404, detail=f"Student by id '{student_id}' was not found"
            )

        return StudentSchema.from_orm(student).dict()


@students_app.post("/students/", responses={"201": StudentSchema})
def create(student_schema: StudentSchema):
    with db.session() as session:
        student_created = Students(**student_schema.dict())

        session.add(student_created)
        session.commit()
        session.refresh(student_created)

        return StudentSchema.from_orm(student_created).dict()


@students_app.delete("/students/{student_id}", responses={"200": None})
def delete(student_id: int):
    with db.session() as session:
        student = session.query(Students).filter_by(id=student_id).first()

        if student is None:
            raise HTTPException(
                status_code=404, detail=f"Student by id '{student_id}' was not found"
            )

        session.delete()
        session.commit()

        return None
