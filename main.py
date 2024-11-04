from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Dict, List
from LinAlgebra.operations import evaluate_expression  # Import the function to evaluate matrix expressions

app = FastAPI()

# Define a request model using Pydantic
class MatrixRequest(BaseModel):
    matrices: Dict[str, List[List[float]]]  # Dictionary of matrix names and their values
    expression: str  # Expression to evaluate, e.g., "A*(B-2)"

@app.post("/evaluate")
async def evaluate_matrices(request: MatrixRequest):
    print(request)
    """
    Endpoint to evaluate matrix expressions based on given matrices and expression.
    """
    matrices = request.matrices
    expression = request.expression

    try:
        # Call the function in operations.py to evaluate the expression
        result = evaluate_expression(expression, matrices)
        return JSONResponse(
            content=jsonable_encoder({"result": result,
                                      "message": {"Success"}}),
        )
    except Exception as e:
        # Handle errors and return a 400 response with error details
        raise HTTPException(status_code=400, detail=str(e))