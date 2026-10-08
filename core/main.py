from fastapi import FastAPI, HTTPException, status,Path, UploadFile,File
from starlette.responses import JSONResponse
from schemas import CreatePersonSchema,ResponsePersonSchema,UpdatePersonSchema

async  def lifespan(app: FastAPI):
    print("applications is started")
    yield
    print("applications is finished")
app = FastAPI(lifespan=lifespan)

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

@app.post("/names",status_code=status.HTTP_201_CREATED,response_model=ResponsePersonSchema)
def create_name(person : CreatePersonSchema):
    name_object = {"id": len(names)+1, "name": person.name}
    names.append(name_object)
    return name_object

@app.put("/names/{name_id}",response_model=ResponsePersonSchema)
def update_name(person : UpdatePersonSchema,name_id:int = Path()):
    for name in names:
        if name["id"] == name_id:
            name["name"] = person.name
            return JSONResponse(content={"details":"update one item successfully "},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object not found")

@app.delete("/names/{name_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_name(name_id:int):
    for name in names:
        if name["id"] == name_id:
            names.remove(name)
            return JSONResponse(content={"details":"remove one item successfully "},status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Object not found")

@app.get("/names}",status_code=status.HTTP_200_OK,response_model=ResponsePersonSchema)
def search_name(q:str):
    if q:
        for name in names:
            if name["name"] == q:
                return {"name":name}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
        # return [item for item in names if item["name"] == q]

@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"name":file.filename,"size":len(content),"type":file.content_type}
