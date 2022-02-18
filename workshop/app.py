from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .database import engine
from .tables import Base

tags_metadata = [
    {
        "name": 'operations',
        "description": "Working with operations"
    },
    {
        "name": 'users',
        "description": "Authentication and authorization"
    },
    {
        "name": 'reports',
        "description": "Import and export of personal incomes and outcomes"
    }
]

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title='Workshop API',
    description='Workshop API is a backend of service for accounting personal incomes and outcomes',
    version='1.0.0',
    openapi_tags=tags_metadata
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
