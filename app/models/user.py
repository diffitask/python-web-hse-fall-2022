from pydantic import BaseModel
from typing import List, Optional
from models.training import Training


class User(BaseModel):
    """Contract for user."""

    name: str = "User"
    female: str = "Usr"
    training_preferences: Optional[List[Training]]
    sports_period: float = 0
    max_training_price: float = 10000
    user_description: Optional[str]
