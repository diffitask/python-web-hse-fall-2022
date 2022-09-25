from models.coach import Coach
from models.training import Training
from models.user import User

from typing import List, Dict


coaches: Dict[str, Coach] = {}

trainings: List[Training] = [
    Training()
]

users: Dict[str, User] = {
    "Louis Armstrong": User(name="Louis", female="Armstrong")
}