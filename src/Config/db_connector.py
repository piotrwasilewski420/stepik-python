from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
load_dotenv()

uri=os.getenv("DB_URI")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASS")
def create_driver():
    return GraphDatabase.driver(uri,auth=(user, password))

driver = create_driver()