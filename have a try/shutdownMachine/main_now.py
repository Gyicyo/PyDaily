"""
    Create At 2024.3.29
    At 18:06
"""
#pylint: disable=E0401,C0103,C0413
import sys
import os
#如果不存在就添加
path = os.getcwd()
sys.path.append(os.path.join(path,'venv'))
sys.path.append(os.path.join(path,'venv\\Lib\\site-packages'))

NAME_SPACE = 40
PID_SPACE = 20
CREATE_TIME_SPACE = 40

import time
import psutil

name = input('你想关掉什么进程:')
print(f"开始寻找： {name}...")

found_processes: set = {proc for proc in
                            psutil.process_iter(['pid','name','create_time'])
                                if name in proc.info['name']}

processes_num = len(list(psutil.process_iter()))

if not found_processes:
    print(f"没有名字中含有“ {name} ”的进程被发现!")
else:
    print('获取到目标进程:')
    print('进程名'.center(NAME_SPACE),'PID'.center(PID_SPACE),'创建时间'.center(CREATE_TIME_SPACE))
    for proc in found_processes:
        name = proc.info['name']
        pid = f'{proc.info['pid']}'
        create_time = time.strftime("%H:%M:%S", time.localtime(proc.info['create_time']))
        print(name.center(NAME_SPACE),pid.center(PID_SPACE),create_time.center(CREATE_TIME_SPACE))

    choice_pid = input("输入一个PID,关闭所有与该进程进程名相同的进程：")
    while True:
        try:
            pid = int(choice_pid)
            target_name = None
            target_proc = psutil.Process(pid)
            if target_proc:
                target_name = target_proc.name()
                break
            else:
                raise ValueError
        except (ValueError,psutil.NoSuchProcess):
            choice_pid = input("输入的PID不合法或未找到该PID,请重新输入：")

    print(f'开始关闭进程，进程名：{target_name}')
    num = 0
    no_close_num = 0
    for proc in [proc for proc in found_processes if target_name == proc.info['name']]:
        try:
            proc.kill()
            num += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            no_close_num += 1
    print(f"成功关闭{num}个进程,{no_close_num}个进程无法被关闭")
    now_processes_num = len(list(psutil.process_iter()))
    other_closed = processes_num - now_processes_num - num
    if other_closed < 0:
        other_closed = 0
    print(f"与此同时，{other_closed}个进程被关闭")

input("按Enter退出...")
print("Exit!")
sys.exit()
