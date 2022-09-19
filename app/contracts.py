from pydantic import BaseModel


class User(BaseModel):
    """Contract for user."""

    name: str
    career: str = None
    training_preferences: str = None
    sports_period: float
    max_training_price: float
    user_description: str = None
