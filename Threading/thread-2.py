import threading
from threading import Thread
import time

lock = threading.Lock()
def timer(name, delay, repetitions):
    lock.acquire()
    print("Started timer: " + name)
    while repetitions > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repetitions -= 1
    print(name + " has completed")
    lock.release()


t1 = Thread(target=timer, args=("Timer 1", 1, 20))
t2 = Thread(target=timer, args=("Timer 2", 1.1, 20))

t1.start()
t2.start()
