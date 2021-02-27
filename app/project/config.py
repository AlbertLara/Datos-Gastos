import os

SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
DEBUG=bool(os.getenv("DEBUG", False))
SECRET_KEY=os.getenv("SECRET_KEY")