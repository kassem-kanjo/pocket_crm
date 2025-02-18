from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# this is so FastAPI can connect to PostgreSQL
engine = create_engine(DATABASE_URL)

# this basically creates database sessions when we need to query the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# class that all database tables will inherit from
Base = declarative_base()

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
