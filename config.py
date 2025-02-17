import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
