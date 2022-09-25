from datetime import datetime
from enum import Enum


class TrainingType(str, Enum):
    "Training type"

    strength_training = "strength training"
    stretching = "stretching"
    dancing = "dancing"


class TrainingDifficulty(str, Enum):
    "Training difficulty"

    easy = "easy"
    medium = "medium"
    hard = "hard"


class Training:
    "Fitness training model"

    def __init__(self, 
                title: str, 
                type: TrainingType,
                duration_mins: int, 
                difficulty: TrainingDifficulty,
                description: str = None):
        self.title = title
        self.type = type,
        self.duration = duration_mins
        self.difficulty = difficulty
        self.description = description


class SheduledTraining:
    "Sheduled training at the particular time"

    def __init__(self,
                training: Training,
                date: datetime, 
                coach_name: str, 
                price: float = 0):
        self.training = training
        self.date = date
        self.coach_name = coach_name
        self.price = price