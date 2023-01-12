import json
from fastapi import APIRouter, Request, Response
from src.Services.employees_service import EmployeesService

employees_routes = APIRouter(prefix='/employees', tags=['employees'])

service = EmployeesService()

@employees_routes.get('/')
async def get_employees(request: Request):
    sort = request.query_params.get('sort')
    filter = request.query_params.get('filter')
    try:
        response = await service.get_employees(sort,filter)
    except Exception as e:
        return Response(status_code=500,content=e,media_type='application/json')
    return Response(status_code=200,content=response,media_type='application/json')

@employees_routes.post('/')
async def create_employee(request: Request):
    employee = await request.json()
    try:
        response,code = await service.create_employee(employee)
        return Response(content=response,status_code=code,media_type='application/json')
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return Response(status_code=409,content=response,media_type='application/json')

@employees_routes.put('/{id}')
async def update_employee(request: Request,id:int):
    try:
        employee = await request.json()
        response,code = await service.update_employee(id,employee)
        return Response(content=response,status_code=code,media_type='application/json')
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return Response(status_code=404,content=response,media_type='application/json')

@employees_routes.delete('/{id}')
async def delete_employee(id:str):
    response,code = await service.delete_employee(id)
    return Response(content=response,status_code=code,media_type='application/json')

@employees_routes.get('/{id}/subordinates')
async def get_subordinates(id:str):
    try:
        response = await service.get_subordinates(id)
        return Response(content=response,status_code=200,media_type='application/json')
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return Response(status_code=404,content=response,media_type='application/json')

@employees_routes.get('/{id}/department')
async def get_departments_by_employees_id(id:str):
    try:
        response = await service.get_department_by_employees_id(id)
        return Response(content=response,status_code=200,media_type='application/json')
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return Response(status_code=404,content=response,media_type='application/json')

    

