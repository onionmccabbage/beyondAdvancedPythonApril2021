# using re-entrant locks (rlocks)
import threading
import time

# we use a class to invoke threads
class MyWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock() # a re-entrant lock
    def modifyA(self):
        with self.rlock: # 'with' will automatically call 'join()'
            print( 'RLock acquired {}, modifying A'.format(self.rlock._is_owned() ) )
            print('{}'.format( self.rlock )) # take a lock at the re-entrant lock
            self.a += 1
            time.sleep(2)
    def modifyB(self):
        with self.rlock: # 'with' will automatically call 'join()'
            print( 'RLock acquired {}, modifying B'.format(self.rlock._is_owned() ) )
            print('{}'.format( self.rlock )) 
            self.b -= 1
            time.sleep(2)
    def modifyBoth(self):
        with self.rlock: # 'with' will automatically call 'join()'
            print( 'RLock acquired {}, modifying A and B'.format(self.rlock._is_owned() ) )
            print('{}'.format( self.rlock )) 
            self.modifyA()
            print('{}'.format( self.rlock )) 
            self.modifyB()
        print('{}'.format( self.rlock ))

if __name__ == '__main__':
    worker = MyWorker()
    worker.modifyBoth()
    worker.modifyA() # different owner?
