from src.Config.db_connector import driver

class EmployeesService:

    async def get_employees(self):
        with driver.session() as session:
            employees = session.run("MATCH (e:Employee) RETURN e").data()
            return [employee['e'] for employee in employees]
