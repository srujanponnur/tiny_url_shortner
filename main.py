from fastapi import FastAPI, Response
import boto3
from pydantic import BaseModel
from dotenv import load_dotenv
from uuid import uuid4
from hashlib import md5
import os

load_dotenv()

client = boto3.client("dynamodb", region_name=os.getenv("AWS_REGION"), aws_access_key_id=os.getenv("ACCESS_KEY"),aws_secret_access_key=os.getenv("SECRET_KEY"))

class URL(BaseModel):
    url: str

app = FastAPI()

@app.get("/{url}", status_code=302)
async def main(response: Response, url: str):
    record = client.get_item(TableName="url_metadata", Key={"target_url":{"S":url}})
    source = record.get("Item").get("source_url")["S"]
    response.headers['Location'] = source

@app.post("/get_short_url")
async def create_url(url: URL):
    result = md5(url.url.encode())
    print(str(result.hexdigest()))
    url_metadata = {
        "source_url": {"S": url.url},
        "user_id": {"S":str(uuid4())},
        "target_url":{"S": str(result.hexdigest())}
    }

    client.put_item(TableName="url_metadata", Item=url_metadata)

    return {"message":"Successfully added the message"}
