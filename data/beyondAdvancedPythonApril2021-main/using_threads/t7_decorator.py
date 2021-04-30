from threading import Lock

# here are some functions which will be used as decorators
def lock_class(methodnames, lockfactory):
    return lambda cls : make_thread_safe(cls, methodnames, lockfactory)

def lock_method(method):
    if getattr(method, '__is_locked', False):
        raise TypeError('Method {} is already locked'.format(method))
    def locked_method(self, *args, **kwargs):
        with self._lock: # the lock is released when 'with' ends
            return method(self, *args, **kwargs)
    lock_method.__name__ = '{}({})'.format('locked method', method.__name__)
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, methodnames, lockfactory):
    init = cls.__init__
    def newinit(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lockfactory
    cls.__init__ = newinit
    # we need need to iterate over the methods of thsi class, making them thread-safe
    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod)
    return cls

# here is a class which we will decorate to make it thread-safe
@lock_class(['add', 'remove'], Lock) # Lock is a lock factory
class ClassDecoratorLocketSet(set): # our class is a set! So it has 'add' and 'remove' methods
    # we can lock specific methods like this
    @lock_method
    def methodToLock(self):
        print('this method will be locekd (and therefore thread-safe)')

if __name__ == '__main__':
    my_set = (4,3,2)
    my_inst = ClassDecoratorLocketSet(my_set)
    # is it locked?
    print(my_inst.add.__is_locked)
    print(my_inst.methodToLock.__is_locked)