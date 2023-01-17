from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from data.model.user import User


def create_user(session: Session, user_id: str, user_name: str):
    session.add(
        User(
            user_id=user_id,
            user_name=user_name
        )
    )

    return HTTPException(status_code=status.HTTP_201_CREATED, detail="201 created")