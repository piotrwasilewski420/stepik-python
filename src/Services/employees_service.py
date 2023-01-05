import json
from src.Config.db_connector import driver

class EmployeesService:

    async def get_employees(self,sort=None,filter=None):
        employees = []
        with driver.session() as session:
            if filter != None:
                employees = session.run("MATCH (e:Employee) WHERE e.name CONTAINS $filter RETURN e", filter=filter).data()
                employees =  [employee['e'] for employee in employees]
            else:
                 employees = session.run("MATCH (e:Employee) RETURN e").data()
                 employees = [employee['e'] for employee in employees]
            if sort != None:
                if sort == 'name':
                    employees = sorted(employees, key=lambda employee: employee['name'])
                elif sort == 'salary':
                    employees = sorted(employees, key=lambda employee: employee['salary'])
                elif sort == 'age':
                    employees = sorted(employees, key=lambda employee: employee['age'])
            return json.dumps(employees)
    
    async def create_employee(self,employee):
        with driver.session() as session:
            employee_exists = session.run("MATCH (e:Employee) WHERE e.name = $name RETURN e", name=employee['name']).data()
            if len(employee_exists) == 0:
                session.run("CREATE (e:Employee {name: $name, salary: $salary, age: $age})", name=employee['name'], salary=employee['salary'], age=employee['age'])
                return json.dumps({'message':'created'}), 201
            else:
                return json.dumps({'message':'exists'}), 409
    
    async def update_employee(self,id,employee):
        with driver.session() as session:
            employee_exists = session.run("MATCH (e:Employee) WHERE e.id = $id RETURN e", id=id).data()
            if len(employee_exists) == 0:
                return json.dumps({'message':'not found'}), 404
            else:
                employee_exists['age'] = employee['age']
                employee_exists['salary'] = employee['salary']
                employee_exists['name'] = employee['name']
                session.run("MATCH (e:Employee) WHERE id(e) = $id SET e.name = $name, e.salary = $salary, e.age = $age", id=id, name=employee_exists['name'], salary=employee_exists['salary'], age=employee_exists['age'])
                if employee['new_department'] != None:
                    session.run("MATCH (e:Employee) WHERE id(e) = $id MATCH (d:Department) WHERE d.name = $department CREATE (e)-[:WORKS_IN]->(d)", id=id, department=employee['new_department'])
                return json.dumps({'message':'updated'}), 200

    async def delete_employee(self,id):
        with driver.session() as session:
            employee_exists = session.run('MATCH (e:Employee) WHERE e.id = $id RETURN e', id=id).data()
            if len(employee_exists) == 0:
                print(employee_exists)
                return json.dumps({'message':'not found'}), 404
            else:
                relations = session.run("MATCH (e:Employee)-[r]-(d) WHERE e.id = $id RETURN e,r,d", id=id).data()
                # session.run("MATCH (e:Employee) WHERE id(e) = $id DETACH DELETE e", id=id)
                return json.dumps({'message':relations}), 200
            
    


