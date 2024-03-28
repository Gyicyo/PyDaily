"""
    created at: 2024-03-28
    At: 13.15 PM
"""

from itertools import batched
from asyncio import AbstractEventLoop
import asyncio
import time
import aiohttp

async def get_status_code(url: str):
    """
        处理单个url请求
    """
    print(f"开始处理url: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"url: {url}, status_code: {response.status}")

async def url_factory(urls: list[str],batch_size=3):
    """
        分批处理urls
    """
    batch = list(batched(urls, batch_size))
    for batch_urls in batch:
        await asyncio.gather(*[get_status_code(url) for url in batch_urls],return_exceptions=True)
        print(f"这是第{batch.index(batch_urls)+1}批数据")

def main():
    """
    主函数
    """
    url_list: list[str] = [
        "https://www.baidu.com",
        "https://www.taobao.com",
        "https://www.jingdong.com",
        "https://www.bilibili.com",
        "https://www.sougou.com",
        "https://www.sohu.com",
        "https://www.qq.com",
        "https://www.163.com",
        "https://www.ifeng.com",
        "https://www.python123.io"
    ]
    time_start = time.perf_counter()
    loop: AbstractEventLoop = asyncio.new_event_loop()
    loop.run_until_complete(url_factory(urls=url_list))
    loop.close()
    time_end = time.perf_counter()
    print(f"总共耗时：{time_end - time_start:.3f}秒")

if __name__ == '__main__':
    main()
