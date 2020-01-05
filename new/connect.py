signal = 1
import threading
import time
from main import startmeasure
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
def getdata():
    startmeasure()
def UIplot():
    pass
# 创建新线程
thread1 = myThread(target = getdata())
thread2 = myThread(target = UIplot())

# 开启新线程
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print ("退出主线程")