from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables del archivo .env

AURA_CONNECTION_URI = os.getenv("NEO4J_URI")
AURA_USERNAME = "neo4j"
AURA_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Client instantiation


def main():
    pass 

