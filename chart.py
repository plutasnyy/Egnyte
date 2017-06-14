from chart_abstract import *
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
class First(Chart):

    def __init__(self):
        self.data_dict={}

    def update(self,new_line):
        action=new_line['eventBody']['action']
        self.data_dict[action]=self.data_dict.get(action,0)+1

    def print_chart(self):
        data=sorted(self.data_dict.items(), key=lambda x: x[1])
        X=[i for i,k in data]
        Y=[k for i,k in data]
        ind=range(1,len(X)+1)

        plt.title("Wykres rzeczy")
        plt.bar(ind,Y,width=0.85, align='center')
        plt.xticks(ind, X, rotation='vertical')
        plt.margins(0.015)
        plt.subplots_adjust(bottom=0.42)
        plt.yscale('log')
        plt.ylim(0,max(Y)*3)

        for x,y in zip(ind,Y):
            plt.text(x,y*1.5,y,ha='center',size='xx-small')

        plt.savefig('lalala',dpi=300)
