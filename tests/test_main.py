import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fibonacci_valid():
    res = client.get("/fib?n=6")
    assert res.status_code == 200
    assert res.json() == {"result": 8}

def test_fibonacci_negative():
    res = client.get("/fib?n=-1")
    assert res.status_code == 422

def test_fibonacci_string():
    res = client.get("/fib?n=abc")
    assert res.status_code == 422