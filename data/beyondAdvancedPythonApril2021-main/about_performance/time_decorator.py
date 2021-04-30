import random
import time
import timeit # might need to pip install this one

# here is a function to be used as a decorator for other functions
def timethis(func):
    '''
    This function will time any other function
    '''
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        run_time = timeit.default_timer() - start_time
        print('The function {} took {} seconds to run'.format(func.__name__, run_time))
        return value
    return function_timer

# here are some functions to be timed
@timethis
def long_runner():
    for x in range(9):
        sleep_time = random.choice(range(1,3))
        time.sleep(sleep_time)

@timethis
def count_up():
    for i in range(1,10000):
        x = i

if __name__ == '__main__':
    long_runner()
    count_up()
