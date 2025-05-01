import requests
from etl import fetch_data, transform_data, load_data
from requests_mock import Mocker
from database import SessionLocal, market_data

def test_fetch_and_transform(requests_mock: Mocker):
    dummy = [{"ticker":"XYZ","date":"2025-04-30","o":"10","h":"12","l":"9","c":"11","v":"1000"}]
    requests_mock.get("https://api.exemplo.com/market/XYZ", json=dummy)
    raw = fetch_data("XYZ")
    recs = transform_data(raw)
    assert recs[0]["symbol"] == "XYZ"
    assert recs[0]["open"] == 10.0

def test_load(db):
    session = SessionLocal()
    load_data([{"symbol":"T","date":"2025-04-30","open":1,"high":1,"low":1,"close":1,"volume":1}])
    result = session.execute(market_data.select()).fetchall()
    assert len(result) == 1

