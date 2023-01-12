from src.Config.db_connector import driver
import json
from src.Services.employees_service import EmployeesService

employee_service = EmployeesService()


class DepartmentsService:
    async def get_departments(self):
        with driver.session() as session:
            departments = session.run("MATCH (d:Department) RETURN d").data()
            departments = [department['d'] for department in departments]
            for department in departments:
                employees = session.run("MATCH (e:Employee)-[r:WORKS_IN]->(d:Department) WHERE d.name = $name RETURN e", name=department['name']).data()
                employees = [employee['e'] for employee in employees]
                department['employees'] = employees
            return json.dumps((departments,department))
