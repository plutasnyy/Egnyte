class Chart():
    '''Base class'''
    def update(self,*args):
        raise NotImplementedError
    def print_chart(self):
        raise NotImplementedError


class First(Chart):

    def __init__(self):
        self.number=0
        self.items=[]

    def update(self,args):
        pass

    def print_chart(self):
        pass
