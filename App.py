from typing import Union
from fastapi import FastAPI, Query

import mysql.connector


conn = mysql.connector.connect(user='root',
                                    password='',
                                    host='localhost',
                                    database='dbmovies')

if conn:
    print('Connected')
else:
    print('error')

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/films")
def get_films():
    cursor = conn.cursor()
    query = 'SELECT * FROM tfilm'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

