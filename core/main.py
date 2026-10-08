from fastapi import FastAPI, HTTPException,status
from starlette.responses import JSONResponse

app = FastAPI()

names =[
    {"id":1,"name":"ali"},
    {"id":2,"name":"ahmad"},
    {"id":3,"name":"hadi"},
    {"id":4,"name":"mohammad"}
]

@app.get("/")
def root():
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"Object not found"})

@app.get("/names")
def get_names():
    return names

@app.get("/names/{name_id}")
def get_one_name(name_id: int):
    for name in names:
        if name["id"] == name_id:
            return name
    return {"detail":"object not found"}

@app.post("/names",status_code=status.HTTP_201_CREATED)
def create_name(name:str):
    name_object = {"id": len(names)+1, "name": name}
    names.append(name_object)
    return {"name":name_object}

@app.put("/names/{name_id}")
def update_name(name_id:int, inname:str):
    for name in names:
        if name["id"] == name_id:
            name["name"] = inname
            return JSONResponse(content={"details":"update one item successfully "},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object not found")

@app.delete("/names/{name_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_name(name_id:int):
    for name in names:
        if name["id"] == name_id:
            names.remove(name)
            return JSONResponse(content={"details":"remove one item successfully "},status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Object not found")

@app.get("/names}",status_code=status.HTTP_200_OK)
def search_name(q:str):
    if q:
        for name in names:
            if name["name"] == q:
                return {"name":name}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
        # return [item for item in names if item["name"] == q]

