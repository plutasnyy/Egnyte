import json
from observer import *

class Data():
    '''class downloading line by line all data from files,
    and sending information to observer'''
    def __init__(self,observer=None):
        if observer is None:
            raise SyntaxError("Data must have the observer")
        else:
            self.observer=observer

    def read_data(self):
        for j in range(0,5):
            for i in open('out/FSE_'+str(j), 'r'):
                new_line=json.loads(i)
                self.observer.send_information(new_line)
        self.observer.send_finnally_information()
