from pydantic import BaseModel
import math

def calculate_total(price : list[float]) -> float:
    """Calculates the total sum of a list of prices."""
    return sum(price)

