import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Kiểm tra kết nối
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Kết nối thành công =))")
except Exception as e:
    print("Kết nối thất bại =(( ", e)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
