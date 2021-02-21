import os

SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
DEBUG=bool(os.getenv("DEBUG",False))