from typing import Optional

from flask_openapi3 import APIBlueprint
from pydantic import BaseModel
from sqlalchemy import select

from api.users.models import Users
from database import db

users_app = APIBlueprint("users_app", __name__)


class UserSchema(BaseModel):
    id: int
    password: str
    email: str
    created_at: str
    updated_at: str
    last_login: Optional[str]
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserList(BaseModel):
    users: list[UserSchema]


@users_app.get("/users", responses={"200": UserList})
def get_users():
    with db.session() as session:
        users_query = session.execute(select(Users)).scalars().all()
        users_list = [
            UserSchema.from_orm(user).dict()
            for user
            in users_query
        ]
        return {"users": users_list}
