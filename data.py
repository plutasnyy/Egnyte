import json
from observer import *

class Data():
    '''class downloading line by line all data from files,
    and sending information to observer'''
    def __init__(self,observer=None):
        self.number_files=33
        self.path='out/FSE_'
        if observer is None:
            raise SyntaxError("Data must have the observer")
        else:
            self.observer=observer

    def read_data(self):
        for j in range(0,self.number_files+1):
            for i in open(self.path+str(j), 'r'):
                new_line=json.loads(i)
                self.observer.send_information(new_line)
        self.observer.send_finnally_information()

    def return_json_file(self,url):
        try:
            temp=[]
            data_file=open(url,'r')
            for i in data_file:
                temp.append(json.loads(i))
            data_file.close()
            return temp
        except: FileNotFoundError
