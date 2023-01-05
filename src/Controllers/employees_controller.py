from fastapi import APIRouter, Request, Response
from src.Services.employees_service import EmployeesService

employees_routes = APIRouter(prefix='/employees', tags=['employees'])

service = EmployeesService()

@employees_routes.get('/')
async def get_employees(request: Request):
    sort = request.query_params.get('sort')
    filter = request.query_params.get('filter')
    response = await service.get_employees(sort,filter)
    return Response(status_code=200,content=response,media_type='application/json')

@employees_routes.post('/')
async def create_employee(request: Request):
    employee = await request.json()
    response,code = await service.create_employee(employee)
    return Response(content=response,status_code=code,media_type='application/json')

@employees_routes.put('/{id}')
async def update_employee(request: Request,id:int):
    employee = await request.json()
    response,code = await service.update_employee(id,employee)
    return Response(content=response,status_code=code,media_type='application/json')

@employees_routes.delete('/{id}')
async def delete_employee(id:str):
    response,code = await service.delete_employee(id)
    return Response(content=response,status_code=code,media_type='application/json')
    

