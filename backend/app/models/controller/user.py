from app.extends.check import BaseModel, Parameter


class UserModel(BaseModel):
    username = Parameter(str)
    password = Parameter(str)
