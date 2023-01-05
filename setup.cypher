CREATE (John:Employee {id: apoc.create.uuid(),name: 'John Doe', age: 30, salary: 100000})

CREATE (Sam:Employee {id: apoc.create.uuid(),name: 'Sam Doe', age: 35, salary: 110000})

CREATE (Sara:Employee {id: apoc.create.uuid(),name: 'Sara Doe', age: 35, salary: 110000})

CREATE (Jasmine:Employee {id: apoc.create.uuid(),name: 'Jasmine Doe', age: 28, salary: 90000})

CREATE (Alex:Employee {id: apoc.create.uuid(),name: 'Alex Doe', age: 40, salary: 120000})

CREATE (Amanda:Employee {id: apoc.create.uuid(),name: 'Amanda Doe', age: 25, salary: 80000})

CREATE (Jane:Employee {id: apoc.create.uuid(),name: 'Jane Doe', age: 25, salary: 80000})

CREATE (Jack:Employee {id: apoc.create.uuid(),name: 'Jack Doe', age: 40, salary: 120000})

CREATE (Jill:Employee {id: apoc.create.uuid(),name: 'Jill Doe', age: 35, salary: 110000})

CREATE (Sales:Department {id: apoc.create.uuid(),name: 'Sales'})

CREATE (Marketing:Department {id: apoc.create.uuid(),name: 'Marketing'})

CREATE (Engineering:Department {id: apoc.create.uuid(),name: 'Engineering'})

CREATE (Sam)-[:WORKS_IN]->(Marketing)

CREATE (Sara)-[:WORKS_IN]->(Marketing)

CREATE (John)-[:WORKS_IN]->(Sales)

CREATE (Amanda)-[:WORKS_IN]->(Engineering)

CREATE (Alex)-[:WORKS_IN]->(Engineering)

CREATE (Jane)-[:WORKS_IN]->(Sales)

CREATE (Jasmine)-[:WORKS_IN]->(Sales)

CREATE (Jack)-[:WORKS_IN]->(Engineering)

CREATE (Jill)-[:WORKS_IN]->(Marketing)

CREATE (John)-[:MANAGES]->(Sales)

CREATE (Sam)-[:MANAGES]->(Marketing)

CREATE (Alex)-[:MANAGES]->(Engineering)

// delete all nodes in database in cypher

// MATCH (n) DETACH DELETE n 

