import threading
import time

def standardThread():
    print('starting a standard thread')
    time.sleep(8)
    print('ending standard thread')

def daemonThread():
    while True:
        print('heartbeat...')
        time.sleep(2)

if __name__ == '__main__':
    s = threading.Thread(target=standardThread)
    d = threading.Thread(target=daemonThread())
    # set d to act as a daemon thread
    d.setDaemon(True)
    d.start()
    s.start()

    # no join()