import pandas as pd
from database import get_connection

def get_df(symbol: str) -> pd.DataFrame:
    sql = f"SELECT * FROM market_data WHERE symbol = '{symbol}' ORDER BY date"
    return pd.read_sql(sql, engine)

def moving_average(symbol: str, window: int = 20) -> float:
    df = get_df(symbol)
    return df['close'].rolling(window).mean().iloc[-1]

def pct_change(symbol: str, periods: int = 1) -> float:
    df = get_df(symbol)
    return df['close'].pct_change(periods).iloc[-1] * 100
