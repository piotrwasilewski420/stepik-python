from fastapi import APIRouter
from src.Services.employees_service import EmployeesService

employees_routes = APIRouter(prefix='/employees', tags=['employees'])

service = EmployeesService()

@employees_routes.get('/')
async def get_employees():
    response = await service.get_employees()
    return response
