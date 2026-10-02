#A **pytest fixture** is a reusable function that prepares data, objects, or setup needed by one or more tests before they run.
from pydantic import BaseModel

# without fixture

def calculate_total(total: list) -> float: # it will return a list
    return sum(total)


