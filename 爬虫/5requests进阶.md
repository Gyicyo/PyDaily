**requests**库的部分进阶使用

[TOC]

#### Session

​	Session能自动帮助处理cookie并持久化一些信息，同时将会使用urllib3的连接池来提高效率

```python
s = requests.Session() # 获取session对象
s.header = header # 给session添加持久header
s.get  /  s.post  / s.put
```

当请求的Response中包含Cookie时，session就会自动存储这些cookie以供使用

直接在请求时上传的header不会被存储



#### SSL证书验证

##### 	requests默认请求证书验证

```python
requests.get(url,verify=False) #关闭证书验证
requests.get(url,verify='path/to/certfile') #上传CAs

s = requests.Session()
s.verify = False
```



##### 客户端证书上传

```python
requests.get(url,cert='/path/client.cert')
```



---

#### 流式下载

```python
import requests

tarball_url = 'https://github.com/psf/requests/tarball/main'

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809',
}

r = requests.get(tarball_url, stream=True,proxies=proxies)
if r.headers.get('Content-length') is not None:
    print('下载内容共'+r.headers.get('Content-length'))
print('开始下载')
chunkAll = 0
all = int(r.headers.get('Content-length'))
print(all)
with open('test.gz','wb') as f:
    for chunk in r.iter_content(chunk_size=4096): # chunk_size指定单次传输量
        if chunk:
            f.write(chunk)
            chunkAll += 4096
            now = int(chunkAll*100/all)
            print('进度:'+now.__str__()+'%')
r.close()
print('完成')
```



需要注意，如果stream=True，那么除非消耗掉response中的所有数据或者调用response.close，否则该连接无法释放回池,这将会降低连接效率。因此可以用with语句来确定response最后会被关闭

```python
with s.get(url) as r :
```



----

#### 流式上传

同样使用with语句

```python
with open('massive-body', 'rb') as f:
    requests.post('http://some.url/streamed', data=f)
```

**注意：**尽量使用二进制方式打开文件，因为请求会自动为内容设置Content-length，如果设为文本方式读取，将会读取文本方式下的长度



---

#### Hooks

​	requests中带有钩子系统。支持在返回response时执行操作

​		钩子方法（Hook method）是一种特殊的函数，它允许在运行时动态地添加、修改或删除功能。钩子方法通常用于在软件开发中的不同阶段或特定事件发生时执行特定的操作。

​		钩子方法的一个常见用例是在软件开发中的插件系统中。插件系统允许开发者在运行时添加新的功能模块，这些模块通常被称为插件。插件可以通过注册钩子方法来定义在特定事件发生时需要执行的操作。当事件发生时，系统会调用相应钩子方法来执行插件定义的操作。

requests中的钩子方法简单来讲就是返回response后会执行的方法

```python
import requests

def print_url(r, *args, **kwargs):
    print(r.url)

def print_staues(r, *args, **kwargs):
    print(r.status_code)


url = 'https://httpbin.org/post'
r = requests.post(url,hooks={'response':[print_url,print_staues]},data= {'key1':'value1','key2':'value2'}) # 可以传多个钩子方法

```



---

#### AuthBase

​		AuthBase允许自定义用户识别方式。通过继承AuthBase类来实现

```python
import requests
from requests.auth import AuthBase

class Auth(AuthBase):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        r.headers['Authorization'] = 'Basic'+ (self.username + ':' + self.password).encode('utf-8').hex() # 在已知Authorization加密方式时可直接使用
        return r

c = requests.get('https://httpbin.org/post', auth=Auth('admin', 'pass'))
```



---

代理

​		上边流式下载GitHub就用到了代理

```python
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('http://example.org', proxies=proxies)

#为指定IP分配代理
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}

```
