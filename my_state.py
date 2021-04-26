class ComputerState(object):
    name = 'state'
    allowed = []
    def switch(self, state):
        if state.name in self.allowed:
            print('Current: {} switching to: {}'.format(self, state.name))
            self.__class__ = state
        else:
            print('Current: {} cannot switch to {}'.format(self, self.name))
    def __str__(self):
        return self.name

class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']

class Off(ComputerState):
    name = 'off'
    allowed = ['on']

class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']

class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']

class Computer():
    def __init__(self, model='super duper'):
        self.model = model
        self.state = Off()
    def change(self, state):
        self.state.switch(state)

if __name__ == '__main__':
    comp = Computer()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    # next line should fail to change state
    comp.change(Hibernate)