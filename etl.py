import os
import sys
import logging
import requests
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal, init_db, market_data, engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s — %(message)s"
)

API_URL = os.getenv("API_URL", "https://api.exemplo.com/market")

def fetch_data(symbol: str) -> list[dict]:
    resp = requests.get(f"{API_URL}/{symbol}", timeout=10)
    resp.raise_for_status()
    return resp.json()

def transform_data(raw: list[dict]) -> list[dict]:
    cleaned = []
    for item in raw:
        try:
            cleaned.append({
                "symbol": item["ticker"],
                "date": datetime.fromisoformat(item["date"]).date(),
                "open": float(item["o"]),
                "high": float(item["h"]),
                "low": float(item["l"]),
                "close": float(item["c"]),
                "volume": int(item["v"])
            })
        except (KeyError, ValueError) as e:
            logging.warning(f"Ignorando registro inválido: {e}")
    return cleaned

def load_data(records: list[dict]):
    session = SessionLocal()
    try:
        if not records:
            logging.info("Nenhum registro para inserir.")
            return
        session.execute(market_data.insert(), records)
        session.commit()
        logging.info(f"{len(records)} registros inseridos com sucesso.")
    except SQLAlchemyError as e:
        session.rollback()
        logging.error(f"Erro ao gravar dados: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    symbol = sys.argv[1] if len(sys.argv) > 1 else "ABC"
    init_db()
    raw = fetch_data(symbol)
    recs = transform_data(raw)
    load_data(recs)
    engine.dispose()

