from threading import Thread

class MyWorkerThread(Thread): # we inherit from Thread
    def __init__(self):
        print('this is an instance of a thread')
        Thread.__init__(self) # call the init method of the super class
    def run(self):
        print('The thread is now running')

if __name__ == '__main__':
    myThread = MyWorkerThread()
    myThread.start()
    myThread.join()
    
        