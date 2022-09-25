from lib2to3.pytree import Node
from typing import Optional

from fastapi import APIRouter

from app.models.user import User


router = APIRouter()


@router.get("/")
def read_root():  # noqa: D103
    return "Hello, New User!"


# path parameters


@router.get("/workouts/{workout_id}")
async def read_item(workout_id: int):  # noqa: D103
    return {"workout_id": workout_id}


# query parameters


@router.get("/users_desires/")
async def read_user(user_id: str, want_to_train: bool = True):
    if not want_to_train:
        return {"item_id": user_id, "desire to train": want_to_train}
    return {"item_id": user_id}


# request body


@router.post("/users/")
async def create_item(user: User):  # noqa: D103
    user_dict = user.dict()

    if user.training_preferences:
        if not user.user_description:
            user_dict.update({"user description": ""})

        user_dict.update({"user_description": "User " + user.name + " preferes: " +
                        user.training_preferences})                    
    return user_dict
