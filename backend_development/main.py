from fastapi import FastAPI
from pydantic import BaseModel,validate_call,ValidationError,StringConstraints,Field
from typing import Annotated


# *****************************
    #  commenting for doing data validation without using BasModel
# *****************************
products = []
app = FastAPI()
class Item(BaseModel):
    name:str = Field(...,min_length=5)
    description:str | None = None
    price:float
    
class ItemResponse(BaseModel):
    status:bool
    message:str
    added_item:str
    
    
@app.post("/items",response_model=ItemResponse)

async def create_item(item:Item):
    if item.name not in products:
        products.append(item.name)
        
    return ItemResponse(
        status=True,
        message="Product added successfully!",
        added_item=item.name
    )
    
    
    
    
    
    
    
# ************************************ Pydantic Use Cases ********************************************
    
# try:
#     product = Item(name="Laptop",description="5th generation I5 Laptop",price=50000)
#     product_without_price = product.model_dump(exclude={'price'})
#     print(product_without_price)
#     print("Product is ready to shipped!")

# except ValidationError as error:
#     print(f"Some Validation Error! {error}")


# # **********************************************************
# # ******** NonBaseModel Validation
# # @validate_call
# # def validate_name(name:Annotated[str,StringConstraints(min_length=5,max_length=25)]):
# #     return name

# # **********************************************************

# # try:
# #     name = validate_name(name="Hari")
# #     print("Name is Valid!")
# # except ValidationError as error:
# #     print(f"name is Invalid! {error}")
