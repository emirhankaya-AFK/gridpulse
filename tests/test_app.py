from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get('/health').json() == {'status': 'ok'}

def test_analyze():
    payload = {'points': [{'timestamp': '2026-01-01T00:00:00Z', 'device_id': 'm1', 'power_kw': 2.0}]}
    response = client.post('/analyze', json=payload)
    assert response.status_code == 200
    assert response.json()['summary']['count'] == 1
