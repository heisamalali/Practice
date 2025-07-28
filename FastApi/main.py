from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
def read_items():
    return {"items": ["item1", "item2"]}


@app.post("/items")
def create_item():
    return {"status": "item created"}


@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"status": f"item {item_id} updated"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"status": f"item {item_id} deleted"}


@app.patch("/items/{item_id}")
def partial_update(item_id: int):
    return {"status": f"item {item_id} partially updated"}