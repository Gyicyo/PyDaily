from typing_extensions import Never
import asyncio
from asyncio import Task
import aiohttp

async def get_staus_code(url: str) -> dict : # 异步发送请求，返回状态码
    print('Getting status code...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Done!')
            return {'url': url, 'status_code': response.status}



async def main() -> Never:

    print('Get  first url...')
    google_code: Task = asyncio.ensure_future(get_staus_code('https://www.google.com/')) # 创建google_Task
    print('Get second url...')
    bilibili_code: Task = asyncio.ensure_future(get_staus_code('https://www.bilibili.com/'))# 创建bilibili_Task
    tasks = [google_code, bilibili_code]
    print('Start to get result')
    done,pending = await asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED) # 完成其中一个任务后立即返回
    for task in done: # done：完成的任务
        result: dict = task.result()
        print(f'{result = }')
        
    for task in pending: # pending：未完成的任务
        task.cancel() # 取消未完成的任务

    exceptions: list = await asyncio.gather(*pending,return_exceptions=True) # 等待剩余任务完成
    #，return_exceptions = True表示不抛出异常，返回为list
    for exception in exceptions: # 异常处理
        if isinstance(exception,asyncio.CancelledError):
            print('Task is cancelled')
        else:
            print(f'{exception = }')

if __name__ == '__main__':
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop() # 获取事件循环
    loop.run_until_complete(main()) # 运行main函数
    #windows直接使用asyncio.run()会导致RuntimeError: Event loop is closed
