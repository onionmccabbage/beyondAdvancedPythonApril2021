import threading
import time
import random

class TicketSeller(threading.Thread):
    ticketsSold = 0
    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.__semaphore = semaphore
        print('Ticket seller started selling tickets')

    def run(self):
        global ticketsAvailable
        running = True # a flag
        while running:
            self.randomDelay()
            self.__semaphore.acquire()
            # have we sole all the tickets?
            if (ticketsAvailable <= 0):
                running = False
            else:
                # lets sell those tickets
                self.ticketsSold += 1
                ticketsAvailable -=1
                print('{} sold one ({} remaining)'.format(self.getName(), ticketsAvailable) )
            self.__semaphore.release()
        # conclusion statement
        print( 'Ticket seller {} sold {} tickets'.format( self.getName(), self.ticketsSold ) )

    def randomDelay(self):
        time.sleep(random.randint(0, 4)/4) # 0, 0.25, 0.5 or 0.75 sec

def main():
    # we need a semaphore
    semaphore = threading.Semaphore()
    sellers = [] # an empty list
    for i in range(4):
        seller = TicketSeller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    ticketsAvailable = 200
    main()