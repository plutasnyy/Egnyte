class Chart():
    '''Base class'''
    def update(self):
        raise NotImplementedError
    def print_chart(self):
        raise NotImplementedError

class First(Chart):
    pass
