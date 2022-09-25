from typing import Optional
from training import Training


class Coach:
    "Coach model"

    def __init__(self, 
                name: str, 
                work_experience: float, 
                desctiption: Optional[str]):
        self.name = name
        self.work_experience = work_experience
        self.desctiption = desctiption
        self.trainings = []

    def add_training(self, 
                    training: Training):
        self.trainings.append(training)