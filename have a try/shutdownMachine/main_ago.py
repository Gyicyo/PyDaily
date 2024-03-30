"""
    Create At 2024.3.29
    At 18:06
"""
#pylint: disable=E0401,C0103,C0413
import sys
import os
#如果不存在就添加
path = os.getcwd()
sys.path.append(f'{path}\\venv')
sys.path.append(f'{path}\\venv\\Lib\\site-packages')
import time
import psutil




name = input('你想关掉什么进程:')
print(f"开始寻找： {name}...")


found_processes: list = [proc for proc in
                            psutil.process_iter(['pid','name','create_time'])
                                if name in proc.info['name']]

processes_num = len(list(psutil.process_iter()))

if not found_processes:
    print(f"没有名字中含有“ {name} ”的进程被发现!")
else:
    print('获取到目标进程:')
    print('进程名'.center(20),'PID'.center(20),'创建时间'.center(40))
    for proc in found_processes:
        name = proc.info['name']
        pid = f'{proc.info['pid']}'
        create_time = time.strftime("%H:%M:%S", time.localtime(proc.info['create_time']))
        print(name.center(20),pid.center(20),create_time.center(40))

    choice_pid = input("输入一个PID,杀死所有与该进程进程名相同的进程：")
    while True:
        try:
            int(choice_pid)

            for proc in found_processes:
                if proc.info['pid'] == int(choice_pid):
                    target_name: str = proc.info['name']
                    break
            if not target_name:
                raise ValueError
            break
        except ValueError:
            choice_pid = input("输入的PID不合法或未找到该PID,请重新输入：")

    print(f'开始杀死进程，进程名：{target_name}')
    num = 0
    no_close_num = 0
    for proc in found_processes:
        if target_name in proc.info['name']:
            try:
                proc.kill()
                num += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                no_close_num += 1
    print(f"成功杀死{num}个进程,{no_close_num}个进程无法被关闭")
    now_processes_num = len(list(psutil.process_iter()))
    other_closed = processes_num - now_processes_num - num
    if other_closed < 0:
        other_closed = 0
    print(f"与此同时，{other_closed}个进程被关闭")


input("按Enter退出...")
print("Exit!")
sys.exit()
