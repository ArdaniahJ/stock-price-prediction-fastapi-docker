from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from model import convert, predict

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    ticker: str
class StockOut(StockIn):
    forecast: dict

# routes
@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI ML Model API!"}

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.get("/predict")
def get_prediction(ticker: str = Query(..., description="Stock ticker symbol")):
    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object


@app.post("/predict")
def predict_stock(payload: StockIn):
    ticker = payload.ticker
    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object
