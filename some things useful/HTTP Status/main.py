"""
    Create At 2024/3/30
    At:19:40 PM
"""
from http import HTTPStatus

ok = HTTPStatus.OK

print(ok.value) # 请求码
print(ok.phrase) # 请求状态信息
print(ok.description) # 请求吗信息描述
