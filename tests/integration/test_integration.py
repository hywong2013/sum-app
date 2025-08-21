# tests/integration/test_api_integration.py
# from fastapi.testclient import TestClient # TestClient 是一個 模擬 API 呼叫環境
import httpx
from app.main import app

# client = TestClient(app)

def test_health():
    r = httpx.get("http://127.0.0.1:8000/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_add_success():
    r = httpx.post("http://127.0.0.1:8000/add", json={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5

def test_add_float_success():
    r = httpx.post("http://127.0.0.1:8000/add", json={"a": 3.2, "b": 0.3})
    assert r.status_code == 200
    assert abs(r.json()["result"] - 3.5) < 1e-12

def test_add_reject_string():
    # 使用 StrictFloat，字串 "2" 會被 Pydantic 拒絕，回傳 422
    r = httpx.post("http://127.0.0.1:8000/add", json={"a": "2", "b": "3"})
    assert r.status_code == 422
