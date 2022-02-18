from fastapi import FastAPI

from workshop.tables import Base

from .api import router

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

app = FastAPI(
    title='Workshop API',
    description='Workshop API is a backend of service for accounting personal incomes and outcomes',
    version='1.0.0',
    openapi_tags=tags_metadata
)
app.include_router(router)
