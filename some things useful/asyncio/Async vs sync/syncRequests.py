"""
    同步请求，与异步相区分
"""

import time
#ingore E0401
import requests #pylint: disable=E0401

def synchronous_request(url: str):
    """
        单个请求
    """
    response = requests.get(url)
    print(f'{url}: status code: {response.status_code}')

def synchronous_requests(urls: list):
    """
        多个请求
    """
    for url in urls:
        synchronous_request(url)


if __name__ == '__main__':
    url_list: list[str]= [
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
    synchronous_requests(url_list)
    time_end = time.perf_counter()
    print(f"Total time: {time_end - time_start:.3f}s")
