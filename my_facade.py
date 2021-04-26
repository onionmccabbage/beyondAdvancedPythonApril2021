# facade hides complexity behind an interface (the facade)

class Coder(object):
    def __init__(self):
        print('Bring coding skills')
    def __isAvailable__(self):
        print('coding skills are available')
        return True
    def bookTime(self):
        if self.__isAvailable__():
            print('coder booking made\n')

class Tester(object):
    def __init__(self):
        print('Preparing test')
    def testing(self):
        print('tests are in place')
    
class Artisan(object):
    def __init__(self):
        print('Designing Stuff')
    def makePrototype(self):
        print('prototyes are ready')
    
class Technician(object):
    def __init__(self):
        print('sound and vision for the team')
    def doStuff(self):
        print('PA project, virtual fridge')
    
# the facade
class Manager(object):
    def __init__(self):
        print('manager says: I can arrange the team')
    def arrange(self):
        self.tester = Tester()
        self.tester.testing()
        self.technician = Technician()
        self.technician.doStuff()
        self.coder = Coder()
        self.coder.bookTime()
        self.artisan = Artisan()
        self.artisan.makePrototype()

class You(object):
    def __init__(self):
        print('we need a team...')
    def askManager(self):
        print('lets contact the manager')
        m = Manager()
        m.arrange()
    def __del__(self):
        print('all done')


if __name__ == '__main__':
    you = You()
    you.askManager()