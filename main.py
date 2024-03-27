from functools import cache
from re import match
from time import sleep
from typing import Callable
from typing_extensions import Never
import asyncio
from asyncio import Task
import requests
from requests import Response
import aiohttp
from aiohttp import ClientResponse

async def get_staus_code(url: str) -> dict :
    print('Getting status code...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Done!')
            return {'url': url, 'status_code': response.status}



async def main() -> Never:

    print('Get  first url...')
    google_code = asyncio.ensure_future(get_staus_code('https://www.google.com/'))
    print('Get second url...')
    bilibili_code = asyncio.ensure_future(get_staus_code('https://www.bilibili.com/'))
    tasks = [google_code, bilibili_code]
    print('Start to get result')
    done,pending = await asyncio.wait(tasks)
    for task in done:
        result: dict = task.result()
        print(f'{result = }')

    print(google_code)
    print(bilibili_code)

if __name__ == '__main__':
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    task: Task = loop.create_task(main())
    loop.run_until_complete(task)