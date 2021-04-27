import threading
import time
import random

# we can have threads defined by functions
def threadworker():
    print('the thread is running')
    time.sleep(2)
    print('the thread is terminating')

def executeThread(i):
    print('Thread {} has started'.format(i))
    sleepTime = random.randint(1,4)
    print('Thread {} has finished executing'.format(i))

if __name__ == '__main__':
    myThread = threading.Thread(target=threadworker)
    myThread.start()
    # myThread.join() # optional, but a good idea
    # run several threads together
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,) ) # pass args as a tuple
        thread.start()
        print('Active Threads: ', threading.enumerate() )
        # thread.join()