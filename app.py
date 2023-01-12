from fastapi import FastAPI
from src.Controllers.employees_controller import employees_routes
from src.Controllers.departments_controller import departments_routes

app = FastAPI(title='project for stepik')

app.include_router(employees_routes)
app.include_router(departments_routes)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

