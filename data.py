import json
from observer import *

class Data():
    '''  '''
    def __init__(self,observer=None):
        if observer is None:
            raise SyntaxError("Data must have the observer")
        else:
            self.observer=observer

    def read_data(self):
        for j in range(0,34):
            for i in open('out/FSE_'+str(j), 'r'):
                new_line=json.loads(i)
                print(new_line['eventBody']['action'],new_line['eventBody']['userId'],new_line['eventHeader']['userAgent'])
                self.observer.send_information(new_line)
        self.observer.send_finnally_information()
