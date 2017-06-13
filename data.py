import json
from observer import *

class Data():
    '''  '''
    def __init__(self,observer):
        self.observer=observer

    def read_data(self):
        for j in range(0,1):
            for i in open('out/FSE_'+str(j), 'r'):
                new_line=json.loads(i)
                self.observer.send_information(new_line)
        self.observer.send_finnally_information()
