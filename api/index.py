from fastapi import FastAPI, HTTPException
# from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
# from .routes import auth
# from .routes import trader
# from .routes import brokerage
# import os
# import platform
# import asyncio
# from .database import get_database


# if platform.system()=='Windows':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# else:
#     asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
# Load environment variables
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection

# db = client.optionsTrading


# Include routers
# app.include_router(auth.router, prefix="/api/auth")
# app.include_router(trader.router, prefix="/api/trader")
# app.include_router(brokerage.router, prefix="/api/brokerage")



@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB"}

# Example endpoint to get items
# @app.get("/items")
# async def get_items():
#     try:
#         # Get count of traders collection
#         trader_collection = await get_database("traders")
#         count = await trader_collection.count_documents({})
#         print(count)
#         # Or get all traders
#         return {"total_traders": count}
#         # return {"message": "Hello World"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# Example endpoint to create an item
# @app.post("/items")
# async def create_item(item: dict):
#     try:
#         global traders
#         result = await traders.insert_one(item)
#         return {"id": str(result.inserted_id)}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
