import asyncio
import aiohttp
from fastapi import FastAPI
import threading


app = FastAPI()

@app.get("/async")
async def async_api_view():
    async with aiohttp.ClientSession() as session:
        print(threading.active_count())
        # Send multiple requests asynchronously
        tasks = []
        for _ in range(200):
            tasks.append(asyncio.ensure_future(fetch_data(session)))

        # Wait for all requests to complete
        results = await asyncio.gather(*tasks)

    return {"results": results}


async def fetch_data(session):
    url = "http://localhost:8000/get/"
    async with session.get(url) as response:
        data = await response.json()
        return data


@app.get("/get")
async def get():
    await asyncio.sleep(10)
    return {"message": "This is an asynchronous response."}