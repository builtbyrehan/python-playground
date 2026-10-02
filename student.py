from pydantic import BaseModel

def get_average(marks: list) -> float:
    return (sum(marks) / len(marks))
