from fastapi import FastAPI
from app.schemas import AnalyzeRequest
from app.analytics import summarize, forecast_next, peak_alert

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    values = [p.power_kw for p in request.points]
    return {
        "summary": summarize([p.model_dump() for p in request.points]),
        "forecast_kw": forecast_next(values, 6),
        "peak_indices": peak_alert(values, 10.0),
    }
