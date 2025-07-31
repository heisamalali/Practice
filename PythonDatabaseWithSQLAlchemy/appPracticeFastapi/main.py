from fastapi import FastAPI

from PythonDatabaseWithSQLAlchemy.appPracticeFastapi.db.models import dbUser
from routers.users import users_router

from db.database import engine

app = FastAPI()
app.include_router(users_router)

dbUser.Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    import  uvicorn
    uvicorn.run("appPracticeFastapi.main:appPracticeFastapi", host='0.0.0.0', port=8000,reload=True)