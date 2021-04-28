import multiprocessing

def myProcFn():
    print('Executing child process (with its own GIL)')

def main():
    print('Executign the main process')
    myProc2 = multiprocessing.Process(target=myProcFn)
    myProc2.start()
    myProc2.join()
    print('child process has terminated')

if __name__ == '__main__':
    main()