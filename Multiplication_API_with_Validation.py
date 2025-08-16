from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

@app.get("/sudhanshu/kumar/xyz")
def add(a: Union[int, str], b: Union[int, str]):
    # Validation
    if not (str(a).isdigit() and str(b).isdigit()):
        return {"error": "Both 'a' and 'b' must be integers"}
    a = int(a)
    b = int(b)
    return {"result": a + b}

class subtractmodel(BaseModel):
    a: Union[int, str]
    b: Union[int, str]

def subtract(a: int, b: int):
    return a - b

def multi(a: int, b: int):
    return a * b

# @app.post("/subtract")
def subtract_numbers(model: subtractmodel):
    # Validation
    if not (str(model.a).isdigit() and str(model.b).isdigit()):
        return {"error": "Both 'a' and 'b' must be integers"}
    return {"result": subtract(int(model.a), int(model.b))}

@app.post("/multiplication")
def multiplication_number(model: subtractmodel):
    # Validation
    if not (str(model.a).isdigit() and str(model.b).isdigit()):
        return {"error": "Both 'a' and 'b' must be integers"}
    return {"result": multi(int(model.a), int(model.b))}
