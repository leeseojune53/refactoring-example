from fastapi import FastAPI
import pymysql
import uuid
import time
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name):
    return {"message": f"Hello {name}"}


@app.post("/feed")
async def post_feed(user_id, user_name):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='refactor', charset='utf8')
    cursor = db.cursor()
    response_data = []
    sql = """
        insert into feed(id, user_id, user_name, comments, created_at) 
        values (%s, %s, %s, %s, %s)
    """ % (uuid.uuid4(), user_id, user_name, "", time.time())
    cursor.execute(sql)

    return {"message": "SUCCESS!!"}


@app.get("/feeds/list")
async def get_feed():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='refactor', charset='utf8')
    cursor = db.cursor()
    response_data = []
    sql = """
            SELECT * FROM feed
            ORDER BY created_at DESC
            LIMIT 100
        """
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            response_data.append(row)

    return response_data


@app.get("/comments/rank")
async def get_commend_rank():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='refactor', charset='utf8')
    cursor = db.cursor()
    comment_data = []
    sql = """
                SELECT comments FROM feed
                ORDER BY created_at DESC
            """
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            json_value = json.loads(row[0])
            for item in json_value:
                comment_data.append(item)

    return sorted(comment_data, key=lambda comment: comment['ttabong'], reverse=True)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
