import asyncio
import aiohttp
import threading
from django.http import JsonResponse
from asgiref.sync import sync_to_async, async_to_sync

async def async_api_view(request):
    async with aiohttp.ClientSession() as session:
        # Send multiple requests asynchronously
        tasks = []
        for _ in range(20):
            tasks.append(asyncio.ensure_future(fetch_data(session)))

        # Wait for all requests to complete
        results = await asyncio.gather(*tasks)

    return JsonResponse({'results': results})


async def fetch_data(session):
    url = 'http://localhost:8000/get/'
    async with session.get(url) as response:
        data = await response.json()
        return data


async def get(request):
    await asyncio.sleep(10)
    return JsonResponse({'message': 'This is an asynchronous response.'})
