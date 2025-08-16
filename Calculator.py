from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

# Input model
class CalculatorInput(BaseModel):
    a: float
    b: float
    #operation: Literal["add", "subtract", "multiply", "DIVIDE"]
    operation : str

@app.post("/calculator")
def calculator(input_data: CalculatorInput):
    firstinput = input_data.a
    secondinput = input_data.b
    op = input_data.operation.lower()

    # Perform operation
    if op == "add":
        result = firstinput + secondinput
    elif op == "subtract":
        result = firstinput - secondinput
    elif op == "multiply":
        result = firstinput * secondinput
    elif op == "divide":
        if secondinput == 0:
            return {"error": "Division by zero is not allowed"}
        result = firstinput / secondinput
    else:
        return {"error": "Invalid operation type. Use add, subtract, multiply, or divide."}

    return {"operation": op, "a": firstinput, "b": secondinput, "result": result}

# Direct test (only runs when executing this file directly)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("calculator:app", host="127.0.0.1", port=8000, reload=True)
