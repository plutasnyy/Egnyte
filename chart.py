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

    def update(self,*args):
        self.number+=1
        self.items.append(args)

    def print_chart(self):
        print(self.items[1])
        print(self.items[-1])
        print(self.number)
