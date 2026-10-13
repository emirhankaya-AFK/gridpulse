import pytest
from app.analytics import forecast_next, peak_alert, summarize
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_forecast_next_empty():
    assert forecast_next([], 3) == [0, 0, 0]

def test_peak_alert():
    assert peak_alert([1, 5, 2], 4) == [1]

def test_summarize_empty():
    assert summarize([])["count"] == 0

def test_analyze_endpoint_one_point():
    response = client.post("/analyze", json={"points": [{"timestamp": "t", "device_id": "d", "power_kw": 5}]})
    assert response.status_code == 200
    assert response.json() == {"count": 1}
