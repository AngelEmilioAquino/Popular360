from databases import Database
import os
from dotenv import load_dotenv

load_dotenv()

Database_URL = os.getenv("DATABASE_URL")
if Database_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment variables")

database = Database(Database_URL)