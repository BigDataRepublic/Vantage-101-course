from fastapi import FastAPI
from pydantic import BaseModel

from typing import Dict

from pipelines import train_pipeline, predict_pipeline

app = FastAPI()


class InputData(BaseModel):
    pass  # ToDo: finish implementation


@app.get("/train/")
def train():
    print("Retraining the model")
    train_pipeline()
    return "Success"


@app.post("/predict/")
def predict(input_data: Dict):
    # input_data = InputDate(**input_data)
    if input_data["mode"] == "test":
        pred = predict_pipeline(X_test=None)
    else:
        pred = predict_pipeline(X_test=input_data)
    return {"results": pred.tolist()}


@app.get("/hello-world/")
def hello_world():
    return "Hello World"
