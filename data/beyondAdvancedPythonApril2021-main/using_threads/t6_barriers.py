import threading
import time
import random

class Mythread(threading.Thread):
    def __init__(self, barrier):
        threading.Thread.__init__(self)
        self.barrier = barrier
    def run(self):
        print('Thread {} is busy...'.format(threading.current_thread()))
        time.sleep(random.randint(1,5))
        print('Thread {} joining but must wait on a barrier ({} waiting)'.format(threading.current_thread(), self.barrier.n_waiting))
        self.barrier.wait()
        print('Barrier lifted, carry on...')

if __name__ == '__main__':
    barrier = threading.Barrier(4)
    threads = []
    for i in range(4):
        thread = Mythread(barrier)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()
