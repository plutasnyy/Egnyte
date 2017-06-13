class observer():
    '''  '''
    def __init__(self):
        self.observers=[]

    def add_observer(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)
            
    def send_information(self,*args):
        for observer in self.observers:
            observer.update(args)

    def send_finnally_information(self):
        for observer in self.observers:
            observer.print_chart()
