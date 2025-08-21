# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, StrictFloat
from src.mycalc.add import add_numbers

class AddRequest(BaseModel):
    a: float
    b: float

# class AddRequest(BaseModel):
#     a: StrictFloat
#     b: StrictFloat

class AddResponse(BaseModel):
    result: float

app = FastAPI(title="Sum API", version="1.0.0")

# 允許前端跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ["*"] / 若要鎖定來源可改成 ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/add", response_model=AddResponse)

def add(req: AddRequest):
    # 使用嚴格型別：若傳來 "2"（字串）會 422 驗證失敗
    result = add_numbers(req.a, req.b)
    return {"result": result}
