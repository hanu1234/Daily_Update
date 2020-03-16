from time import sleep
import threading


def demo():
    cond = True
    while cond:
        print("Running thread")
        sleep(10)
        cond = False
    print("stopped thread")


t1 = threading.Thread(target=demo, )
t1.start()
t1 = threading.Thread(target=demo, )
t1.start()
t1 = threading.Thread(target=demo, )
t1.start()

print(threading.active_count())
sleep(30)
print(threading.active_count())


