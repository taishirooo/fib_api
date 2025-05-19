from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/fib")
def get_fibonacci(n: int = Query(..., gt=0)):
    try:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return {"result": b if n > 1 else 1}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid input")