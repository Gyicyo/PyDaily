"""
    created at: 2024-03-28
    At: 23.18 PM
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
import logging

logging.basicConfig(format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',#格式
                    filename='example.log', #日志文件名
                    level=logging.DEBUG, #日志级别
                    datefmt='%Y-%m-%d %H:%M:%S', #时间格式
                    encoding='utf-8', #编码格式
                    filemode='w') #文件输入模式(默认为追加模式，这里改为覆盖模式)

logging.debug('This is a debug message')
logging.warning('This is a warning message')
logging.error('This is an error message')