import os
from multiprocessing import Process
import time
from random import randint

def run_task1(t):
    print(f"Task 1 is running:{os.getpid()},will done in {t} seconds")
    time.sleep(t)
    print("Task 1 is done")

def run_task2(t):
    print(f"Task 2 is running:{os.getpid()},will done in {t} seconds")
    time.sleep(t)
    print("Task 2 is done")

if __name__ == '__main__':
    p1 = Process(target=run_task1, args=(randint(1, 5),))
    p2 = Process(target=run_task2, args=(randint(1, 5),))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All tasks are done")
