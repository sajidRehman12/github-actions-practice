from fastapi import FastAPI
app = FastAPI()




@app.get("/")
def read_root():   
     return {"Hello": "World"}   



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



@app.post("/items/")
def create_item(name: str): 
     return {"name": name}    



@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):    
     return {"item_id": item_id, "name": name}    



@app.delete("/items/{item_id}")
def delete_item(item_id: int):    
     return {"item_id": item_id, "status": "deleted"}
