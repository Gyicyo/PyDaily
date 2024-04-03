

[TOC]



​		selenium是主流的Web UI自动化测试库之一。selenium由一些插件和类库组成：selenium IDE（浏览器的录制与回放）、selenium Grid（在多台计算机或异构环境中进行测试）、selenium webDriver（客户端API接口，控制浏览器驱动）。

​		appium（application+selenium）是移动平台上主流的自动化测试工具之一。封装了标准selenium客户端类库，为用户提供常见的json格式的selenium命令，以及额外的移动设备控制相关的命令。

在爬虫领域 selenium 同样是一把利器，能够解决大部分的网页的反爬问题。

---

### selenium



​		Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera，Edge等。这个工具的主要功能包括：测试与浏览器的兼容性——测试应用程序看是否能够很好得工作在不同浏览器和操作系统之上。


#### 安装

selenium IDE 在各浏览器的插件中找

selenium webDriver执行

```bash
.\pip install selenium
```

下载

#### 基本使用

```python
import selenium
from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By
import time

service = service.Service('C:/Users/Gyi/Desktop/python爬虫/msedgedriver.exe') # 导入浏览器驱动

options = webdriver.EdgeOptions()
options.add_experimental_option('detach',True) # 保持浏览器运行

driver = webdriver.Edge(options,service=service) # 使用Edge驱动
# 打开百度首页
driver.get("https://www.baidu.com")
```

selenium需要导入相应的浏览器驱动来建立连接。支持常见的Chrome、firefox、Edge等浏览器

只需要去浏览器下载对应版本的浏览器驱动即可(确保驱动版本与当前浏览器版本一致)。

**注：**此外，selenium并不必须手动导入浏览器驱动。它会自己检索已安装的浏览器驱动并使用



默认情况下，执行完毕后浏览器会立即关闭，通过添加option可以设置浏览器持续运行



接下来，要模拟浏览器行为进行操作，需要先查找相应的元素，然后进行相关操作

#### 元素定位

selenium支持的查询定位方式有很多种

- id定位 
- name定位
- class定位
- tag定位
- xpath定位
- css定位
- link定位
- partial_link定位

具体使用语法可以参考[自动化测试之八大元素定位方式（python3.10+selenium4）_python自动化元素定位-CSDN博客](https://blog.csdn.net/Little_Carter/article/details/128859268?ops_request_misc=%7B%22request%5Fid%22%3A%22170118277716800182771353%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=170118277716800182771353&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-128859268-null-null.142^v96^pc_search_result_base3&utm_term=selenium4定位元素的方法&spm=1018.2226.3001.4187)



```python
driver.find_element(By.ID,'kw') # 定位一个id为kw的元素

driver.find_elements(By.CLASSNAME,'a') # 定位一组class名为a的元素
```



find_element和find_elements的区别：

​		find_element未定位成功会抛出异常，而find_elements会返回一个空列表



#### 浏览器控制

##### 修改窗口

```python
#指定宽高
driver.set_window_size(600, 800)
#全屏
driver.maximize_window()
```

##### 前进/后退

这里指的是同一页面的前进/后退（←和→）

```python
driver.back() #后退
driver.forword() #前进

#要在同一窗口打开两个网站，只需要执行两个get
driver.get('https://www.baidu.com')
driver.get('https://cn.bing.com')

#若要在不同窗口打开两个页面，执行以下操作
driver.get('https://www.baidu.com')
js = "window.open('https://cn.bing.com')"
driver.execute_script(js) #同步执行JavaScript
```

##### 刷新

```python
driver.refresh()
```

##### 切换当前窗口

```python
# 获取打开的多个窗口（旧到新排列）
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])
#查看当前driver的窗口
driver.current_window_handle
```

driver不会自动切换窗口，哪怕新打开了一个窗口。



##### 关闭窗口

```python
driver.close() #关闭当前driver的窗口
```



#### 常用操作

以模拟百度搜索为例子进行介绍

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge import service
import time

service = service.Service('C:/Users/Gyi/Desktop/python爬虫/msedgedriver.exe')

driver = webdriver.Edge(service=service)

driver.get("https://www.baidu.com")
driver.maximize_window()

element= driver.find_element(By.ID,"kw") # 查询id为kw的元素（百度的搜索框）

element.send_keys('wdmd') # 输入内容

#两种提交方法。1、直接提交。 2、点击搜索
element.submit() #相当于键盘的enter，提交内容

driver.find_element(By.ID,'su').click() #点击按钮搜索

element.clear() #清空内容

if element.is_displayed(): # 判断元素是否可见
    print('显示')
else:
    print('不显示')

element.size # 元素宽高
element.text # 元素text属性
element.get_attribute('id') # 获取元素指定内容

```

到这里就可以实现基本的自动化了

#### 实例

##### 使用selenium登录ccnu并查询用户信息

```python
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge import service
import requests
from requests.cookies import RequestsCookieJar
import User

s = requests.session()

service = service.Service('C:/Users/Gyi/Desktop/python爬虫/msedgedriver.exe')

driver = webdriver.Edge(service=service)
driver.get('https://account.ccnu.edu.cn/cas/login?service=http%3A%2F%2Fone.ccnu.edu.cn%2Fcas%2Flogin_portal')

driver.find_element(By.ID, 'username').send_keys(User.id)
driver.find_element(By.ID, 'password').send_keys(User.password)
driver.find_element(By.NAME,'submit').click()

c = driver.get_cookies() # 获取当前对话中的cookie

for p in c:
    m = RequestsCookieJar()
    m.set(p['name'], p['value'], domain=p['domain'], path=p['path'])
    s.cookies.update(m)


s.headers.update({'Authorization':f'Bearer {s.cookies["PORTAL_TOKEN"]}'})
r = s.post('http://one.ccnu.edu.cn/user_portal/index')
print(r.text)
```

这样写很简单，但是在能直接请求的情况下不推荐使用selenium进行数据获取。相对于直接请求速度会慢很多，而且selenium主要用来进行自动测试

##### 百度搜索内容后点击每一个搜索结果

```python
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import service
import time

service = service.Service('C:/Users/Gyi/Desktop/python爬虫/msedgedriver.exe')

driver = webdriver.Edge(service=service)

# 打开百度首页
driver.get("https://www.baidu.com")
driver.maximize_window()
# 定位搜索框，输入关键词 "wdmd"，然后按 Enter 键
search_box = driver.find_element("name", "wd")
search_box.send_keys("wdmd")
driver.find_element(by=By.ID, value="su").click()

# 等待一段时间，确保搜索结果加载完成
time.sleep(2)

# 定位所有搜索结果的标题元素
results = driver.find_elements(by=By.CSS_SELECTOR,value='.c-title a')

# 遍历搜索结果并点击每个结果
for result in results:
    original_window = driver.current_window_handle

    result.click()

    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(2)
    driver.close()

    driver.switch_to.window(original_window)

driver.quit()
```



#### 鼠标控制

在webdriver 中，鼠标操作都封装在ActionChains类中

```python
from selenium.webdriver import ActionChains

driver = webdriver.Edge(service=service)

# 移动到指定位置并双击。perform是每一个鼠标操作的执行函数
ActionChains(driver).move_by_offset(150,150).double_click().perform()

#移动到指定元素并右击
ActionChains(driver).move_to_element(element).content_click().perform()

#仅移到位置（悬停）
ActionChains(driver).move_to_element(element).perform()

# 拖动e到e2位置
ActionChains(driver).drag_and_drop(e,target=e2)
```



#### 键盘控制

webdriver包含了所有常见的键位，包括组合键

```python
from selenium.webdriver.common.keys import Keys

e = driver.find_element(By.ID, 'kw')
time.sleep(2)
e.send_keys(Keys.CONTROL + 'v')
```



#### 元素等待

有时候某个元素需要加载才能出现，这时就需要等待

##### 显示等待

​		设置一个超时时间，每隔一段时间就去检测一次该元素是否存在，如果存在则执行后续内容，如果超过最大时间（超时时间）则抛出超时异常（`TimeoutException`）。显示等待需要使用 `WebDriverWait`，同时配合 `until` 或 `until_not` 。



WebDriverWait构造的3个参数：

- driver ：浏览器驱动
- timeout : 最大等待时间
- `poll_frequency`：每次检测的间隔时间,默认0.5s

until

指定预期条件的判断方法，在等待期间，每隔一段时间调用该方法，判断元素是否存在，直到元素出现。`until_not` 正好相反，当元素消失或指定条件不成立，则继续执行后续代码

expected_conditions中包含多种预期条件判断方法，用于传入method。

```python
until(method, message='')
until_not(method, message='')
```



```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
        (WebDriverWait(driver, 5,0.5).
                until(EC.title_is("百度一下，你就知道"),message='未发现指定title'))
except Exception as e :
        print(+e.__str__())
print('向下执行')
time.sleep(5)
driver.quit()
```

检测失败会抛出TimeoutException异常

##### 隐式等待

隐式等待是在整个 WebDriver 的生命周期中等待一定的时间。即在查找元素时都会等待一段时间。若没找到，抛出NoSuchElementException异常

```python
from selenium.common.exceptions import NoSuchElementException

driver.implicitly_wait(5) # 设置隐式等待时间

try:
       e = driver.find_element(By.ID, 'ke')
except NoSuchElementException as e :
        print(e.msg)
```



#### 表单切换

​		很多页面也会用带 `frame/iframe` 表单嵌套（网页里套一个网页），对于这种内嵌的页面 `selenium` 是无法直接定位的，需要使用 `switch_to.frame()` 方法将当前操作的对象切换成 `frame/iframe` 内嵌的页面。

```python
driver.implicitly_wait(5)
e = driver.find_element(By.XPATH,'/html/body/iframe') # 定位iframe

driver.switch_to.frame(e) # 转换到对应iframe表单

driver.find_element(By.ID,'dw').click() # 现在是在iframe表单中进行搜索
```



#### 弹窗处理

`JavaScript` 有三种弹窗 `alert`（确认）、`confirm`（确认、取消）、`prompt`（文本框、确认、取消）。

处理方式：先定位（`switch_to.alert`自动获取当前弹窗），再使用 `text`、`accept`、`dismiss`、`send_keys` 等方法进行操作

```python
driver.find_element(By.ID,'alert').click()
alert = driver.switch_to.alert
alert.accept() #确定
alert.dismiss() #取消
alert.send_keys('123') #输入文本 Firefox能用，其他浏览器似乎并不能执行
```



#### 文件操作

##### 上传文件

常见的 web 页面的上传，一般使用 `input` 标签或是插件（`JavaScript`、`Ajax`），对于 `input` 标签的上传，可以直接使用 `send_keys(路径)` 来进行上传。

```python
driver.find_element(By.TAG_NAME,'input').send_keys("filePath")
```

测试用html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <input type="file" name="">
</body>
</html>

```



##### 下载文件

以firefox为例下载一个图片文件

```python
from selenium import webdriver
from selenium.webdriver.firefox import service
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import User

options = webdriver.FirefoxOptions()
service = service.Service(User.firePath)
profile.set_preference("browser.download.dir", "C:\\Users\Gyi\Downloads") # 下载地址
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream") # 保存类型
driver = webdriver.Firefox(options=profile,service=service)

driver.get('https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%83%9F%E8%8A%B1&step_word=&hs=0&pn=0&spn=0&di=46137345&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=1244081536%2C2149495260&os=2804815467%2C2066679620&simid=3468297450%2C255683807&adpicid=0&lpn=0&ln=1508&fr=&fmq=1701427690534_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=11&oriquery=&objurl=https%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%3A%2F%2Fdingyue.ws.126.net%2F2023%2F1201%2Fc0da8ecfj00s4z4jf01udc000tc00ksm.jpg%26thumbnail%3D660x2147483647%26quality%3D80%26type%3Djpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B8mn_z%26e3Bv54AzdH3F1yAzdH3Fw6ptvsjAzdH3FIKSJSGLAaccndRam_z%26e3Bip4s&gsm=1e&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&dyTabStr=MCwzLDEsMiw2LDQsNSw3LDgsOQ%3D%3D&lid=10690575932274825479')

e = driver.find_element(By.CSS_SELECTOR,'.btn-download')
e.click()
```



#### Cookies操作



cookies 是识别用户登录与否的关键，爬虫中常常使用 selenium + requests 实现 cookie持久化，即先用 selenium 模拟登陆获取 cookie ，再通过 requests 携带 cookie 进行请求。

webdriver 提供 cookies 的几种操作：读取、添加删除。

- get_cookies：以字典的形式返回当前会话中可见的 cookie 信息。
- get_cookie(name)：返回 cookie 字典中 key == name 的 cookie 信息。
- add_cookie(cookie_dict)：将 cookie 添加到当前会话中
- delete_cookie(name)：删除指定名称的单个 cookie。
- delete_all_cookies()：删除会话范围内的所有 cookie。



调用javaScript

给出一个循环向下滑动进行懒加载网页的demo

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://so.csdn.net/so/search?q=selenium4%20firefox%20option&t=&u=&urw=")
driver.maximize_window()
sleep(1)

for i in range(20,110,5):
    sleep(1)
    print(i.__str__())
    target = driver.find_element(By.XPATH,f"//div[@class='list-item' and @i='{i}']")
    driver.execute_script('arguments[0].scrollIntoView();',target) # （要执行的javaScript，参数）,参数可有可无
sleep(12)

driver.execute_script('window.scrollTo(0,500);') # 滑动到（0，500）
```



#### 截图

```python
driver.get_screenshot_as_file('path')
```



#### 隐藏指纹特征 

​		`selenium` 对于部分网站来说十分强大，但它也不是万能的，实际上，`selenium` 启动的浏览器，有几十个特征可以被网站检测到，轻松的识别出你是爬虫。

手动打开https://bot.sannysoft.com/,再用selenium打开，即可看到其识别出了selenium特征

解决这个问题的关键，实际就是一个 `stealth.min.js` 文件。在 `Python` 中使用的话需要单独执行这个文件，该文件获取方式需要安装 `node.js`。执行下列指令来生成该文件

```bash
npx extract-stealth-evasions
```

```python
import time
import selenium.webdriver.chromium.options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge import service
import requests
from requests.cookies import RequestsCookieJar
import User

service = service.Service(User.driverPath)
options = selenium.webdriver.EdgeOptions()

driver = webdriver.Edge(service=service,options=options)

with open(r'D:\PyCharm\study\venv2\stealth.min.js') as f:
    js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

driver.get('https://bot.sannysoft.com/')
driver.save_screenshot('C:\\Users\Gyi\Downloads\page.png')
time.sleep(1)
```

执行后可以发现已经检测不到selenium特征了



#### 接管浏览器

接管浏览器即用selenium连接已存在的浏览器，以此来跳过自动化较为困难的部分

这里用Edge来实现，其他浏览器相似

创建一个浏览器快捷方式的副本，打开属性，修改其目标

需要添加以下参数

- `--remote-debugging-port` 是指定运行端口，只要没被占用就行
- `--user-data-dir` 指定运行浏览器的运行数据，不影响系统原浏览器的数据

```bash
msedge.exe --remote-debugging-port=9222 --user-data-dir="D:\python\seleniumEdge"
```

将目标值更换为上述指令（两个参数值自己改）

运行浏览器副本到任意网址

```python
options = webdriver.EdgeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Edge(options=options)
driver.find_element(By.ID,'kw').send_keys('123321') # 这里打开的是百度
time.sleep(2)
```

python执行上述代码，发现已经成功接管已打开的浏览器，并且没有出现“Edge正由自动测试软件控制”，就像真人打开一样



---



### appium

​	appium使用方法与selenium相差不大，但是需要进行许多环境配置



#### 环境配置

​	最基础的，下载sdk和jdk，然后配置环境变量

- ANDROID_HOME变量，即Android sdk的路径。直接配置在用户变量里
- adb环境，即sdk中的platform-tools路径，放在Path里



​	然后，在Appium官网下载Appium Server。建议下载有GUI的

​	Appium默认监听4723端口，直接启动即可

​	

appium使用真机进行测试需要手机开启开发者模式。

- 小米：在开发者选项里，把USB调试（安全设置）打开即可，允许USB调试修改权限或模拟点击
- OPPO：在开发者选项里，把“禁止权限监控”打开即可

下面为一个基本的参数配置

```python
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '13',  # 手机安卓版本
    'deviceName': 'myPhone',  # 设备名，安卓手机可以随意填写
    'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': '.MainActivityV2',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element(By.ID,'avatar').click() # 点击左上角的头像
time.sleep(5)
driver.quit()
```



除了在python上自己写，也可以直接去下载Appium Inspector。这个可以用来写测试脚本，但是感觉用来找元素更多

配置：（配置所需能力JSON会自己生成）

![ROFJX.png](https://pic5.58cdn.com.cn/nowater/webim/big/n_v250b6fa16dad44dd3bc4ebb1cca698739.png)

和自己写的脚本一样，启动需要先连接手机，就像Android studio调试那样



包和Activity

启动App，启动哪个Activity，需要先获取app的包名和当前的activity

配置完adb环境后，连接上手机，打开要测试的app到指定的Activity，在命令行输入

```bash
adb shell dumpsys activity recents | find "intent={"
```

即可检查当前手机正在运行的app的包名和activity

启动后会在手机上下载一个软件，下载即可

使用 Inspector 时点击响应会很慢，把下载的东西允许耗电即可



#### 华师匣子蹭课小测试

```python
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '13',  # 手机安卓版本
    'deviceName': 'Gyi',  # 设备名，安卓手机可以随意填写
    'appPackage': 'net.muxi.huashiapp',  # 启动APP Package名称
    'appActivity': '.ui.main.SplashActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']

e = driver.find_elements(By.XPATH,"//android.widget.RelativeLayout[android.widget.TextView[@text='蹭课']]")
if len(e) != 0:
    e[0].click()
    teacher = driver.find_element(By.XPATH,"//android.widget.EditText[@text='请输入课程名称']")
    teacher.send_keys('原理')
    button = driver.find_element(By.XPATH,"//android.widget.TextView[@text='搜索课程']")
    button.click()
    touch = TouchAction(driver)
    for i in range(4):
        driver.swipe(width/2,height*3/4,width/2,height/8,100)
        time.sleep(0.2)
    e = driver.find_element(By.XPATH,"//android.widget.RelativeLayout[.//android.widget.TextView[contains(@text,'互联网产品')]]/android.widget.Button")
    e.click()
    e = driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='转到上一层级']")
    e.click()
    e = driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='转到上一层级']")
    e.click()
    e = driver.find_element(By.XPATH,"//android.widget.TextView[@text='课程表']")
    e.click()
else:
    driver.quit()
driver.quit()
```

