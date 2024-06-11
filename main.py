import web_scraping
import model
from fastapi import FastAPI

app = FastAPI()
test = web_scraping.Web_scraping()



@app.get("/beograd")
async def get_data(day=1):
    data = test.web_scraping(day)
    headers = data[0]
    json_data = [dict(zip(headers, row)) for row in data[1:]]
    return json_data


@app.get("/novisad")
async def get_data(day=1):
    data = test.web_scraping(day,"novi_sad")
    headers = data[0]
    json_data = [dict(zip(headers, row)) for row in data[1:]]
    return json_data



@app.get("/kraljevo")
async def get_data(day=1,):
    data = test.web_scraping(day,"kraljevo")
    headers = data[0]
    json_data = [dict(zip(headers, row)) for row in data[1:]]
    return json_data

@app.get("/nis")
async def get_data(day=1):
    data = test.web_scraping(day,"nis")
    headers = data[0]
    json_data = [dict(zip(headers, row)) for row in data[1:]]
    return json_data

@app.get("/kragujevac")
async def get_data(day=1):
    data = test.web_scraping(day,"kragujevac")
    headers = data[0]
    json_data = [dict(zip(headers, row)) for row in data[1:]]
    return json_data