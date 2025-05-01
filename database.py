import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data.db")

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
metadata = MetaData()

market_data = Table(
    "market_data", metadata,
    Column("id", Integer, primary_key=True),
    Column("symbol", String, index=True),
    Column("date", Date),
    Column("open", Float),
    Column("high", Float),
    Column("low", Float),
    Column("close", Float),
    Column("volume", Integer),
)

def init_db():
    metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
    print("✅ Banco inicializado em", DATABASE_URL)

