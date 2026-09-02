from fastapi import FastAPI
from sqlalchemy import text
from database import engine




app=FastAPI()

@app.get("/")
def read_root():
    return{
        "Message":"Student management API is running"
    }

@app.get("/health")
def database_test():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return{
            "status":"success",
            "message":"database working"
        }

    except Exception as e:
        return{
            "status":"error",
            "message":str(e)
  
        }