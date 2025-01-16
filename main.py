from fastapi import FastAPI, HTTPException
from models import ItemPayload

app = FastAPI()
grocery_list: dict[int, ItemPayload] = {}


#route for adding items 
# Route to add a item
@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int):
    if quantity <= 0:                                                                                                                                        
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")
    # if item already exists, we'll just add the quantity.
    # get all item names
    items_ids = {item.item_name: item.item_id if item.item_id is not None else 0 for item in grocery_list.values()}
    if item_name in items_ids.keys():
        # get index of item_name in item_ids, which is the item_id
        item_id = items_ids[item_name]
        grocery_list[item_id].quantity += quantity
# otherwise, create a new item
    else:
        # generate an ID for the item based on the highest ID in the grocery_list
        item_id = max(grocery_list.keys()) + 1 if grocery_list else 0
        grocery_list[item_id] = ItemPayload(
            item_id=item_id, item_name=item_name, quantity=quantity
        )

    return {"item": grocery_list[item_id]}

#route to list specific items by ID 
@app.get("/items/{items_id}")
def list_item(item_id: int) -> dict[str, ItemPayload]:
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="item not found")
    return {"item": grocery_list[item_id]} 

#route to list all items
@app.get("/items")
def list_items() -> dict[str, dict [int, ItemPayload]]:
    return {"items": grocery_list}

# Route to delete a specific item by ID 
@app.delete("/items/{item_id}")
def delete_item(item_id: int ):	
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="item not found")
    del grocery_list[item_id]
    return {"result": "items successfully deleted from the list "}

# Route to remove some quantity of a specific item by ID 
@app.delete("/items/{item_id}/{quantity}")
def remove_quantity(item_id: int, quantity: int):
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="item not found")
    #if the quantity to be removed is greater than the quantity of the item, delete the item
    if grocery_list[item_id].quantity <= quantity:
        del grocery_list[item_id]
        return {"result" : "item successfully deleted from the list"}
    #otherwise, subtract the quantity from the item
    else:
        grocery_list[item_id].quantity -= quantity
        return {"result": f"{quantity} items removed."}
    
	# Route to update the quantity of a specific item by ID
    
@app.put("/items/{item_id}/{quantity}")
def update_quantity(item_id: int, quantity: int):
	if item_id not in grocery_list:
		raise HTTPException(status_code=404, detail="item not found")
	grocery_list[item_id].quantity = quantity
	return {"result": "quantity updated successfully"}

    
