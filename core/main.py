from fastapi import FastAPI
app = FastAPI()

names =[
    {"id":1,"name":"ali"},
    {"id":2,"name":"ahmad"},
    {"id":3,"name":"hadi"},
    {"id":4,"name":"mohammad"}
]

@app.get("/")
def root():
    return{"message":"hello wolrld"}

@app.get("/names")
def show_nams():
    return names