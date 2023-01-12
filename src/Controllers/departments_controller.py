from fastapi import APIRouter, Request, Response
from src.Services.departments_service import DepartmentsService
from src.Services.employees_service import EmployeesService
import json

departments_routes = APIRouter(prefix='/departments', tags=['departments'])

service = DepartmentsService()
employees_service = EmployeesService()

@departments_routes.get('/')
async def get_departments():
    try:
        response = await service.get_departments()
        return Response(content=response,status_code=200,media_type='application/json')
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return Response(status_code=404,content=response,media_type='application/json')

@departments_routes.get('/{id}/employees')
async def get_employees_by_department_id(id:str):
    try:
        response = await employees_service.get_employees_by_department_id(id)
        return Response(content=response,status_code=200,media_type='application/json')
    except Exception as e:
        response = json.dumps({'message':e.args[0]})
        return Response(status_code=404,content=response,media_type='application/json')