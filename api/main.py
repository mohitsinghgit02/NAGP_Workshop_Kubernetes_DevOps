from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()


@app.get("/")
def index():
    return {"sucess": True}


@app.get("/api/items")
def read_items():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"items": rows}
