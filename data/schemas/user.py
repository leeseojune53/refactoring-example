from pydantic import BaseModel, constr


class CreateUser(BaseModel):
    user_id: constr(min_length=1, max_length=36)
    user_name: constr(min_length=1, max_length=20)
