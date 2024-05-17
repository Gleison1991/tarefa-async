from django.http import HttpResponse
import asyncio
import httpx
from asgiref.sync import async_to_sync

async def minha_view(request):
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)
    return HttpResponse("Requisição concluída!")
