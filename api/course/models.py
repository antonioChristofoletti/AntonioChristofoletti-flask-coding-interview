from sqlalchemy.orm import Mapped, mapped_column

from api import db
from api.db import Base


class StudentCourseEnrollment(db.Model):
    __tablename__ = "student_course_enrollment"

    student_id = db.Column(
        db.Integer, db.ForeignKey("student.id"), nullable=False, primary_key=True
    )
    course_id = db.Column(
        db.Integer, db.ForeignKey("course.id"), nullable=False, primary_key=True
    )

    enrollment_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    num_credits: Mapped[int] = mapped_column(nullable=False)

    student = db.relationship("Student", backref="enrollments")
    course = db.relationship("Course", backref="enrollments")


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    professor_name: Mapped[str] = mapped_column(nullable=False)
    max_students: Mapped[int] = mapped_column(nullable=False)

    min_course_credits: Mapped[int] = mapped_column(nullable=False)
