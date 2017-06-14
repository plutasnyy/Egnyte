from chart_abstract import *
import matplotlib.pyplot as plt

class First(Chart):

    def __init__(self):
        self.dict={}

    def update(self,new_line):
        action=new_line['eventBody']['action']
        self.dict[action]=self.dict.get(action,0)+1

    def print_chart(self):
        self.dict=sorted(self.dict.items(), key=lambda x: x[1])
        X=[ X for (X,Y) in self.dict]
        Y=[ int(Y) for (X,Y) in self.dict]
        ind=range(1,len(X)+1)
        print(len(X),len(Y))
        X=range(len(X))
        plt.bar(ind,Y)
        plt.xticks(ind,X)
        plt.yscale('log')
        plt.savefig('lol.jpg')
