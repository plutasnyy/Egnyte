from chart_abstract import *
import matplotlib.pyplot as plt

class Quantity_of_actions_with_source(Chart):

    def __init__(self):
        self.data_dict={}
        self.actions=[]
        self.sources=[]

    def update(self,new_line):
        action=new_line['eventBody']['action']
        source=new_line['eventBody']['actionSource']

        if action not in self.actions:
            self.actions.append(action)
        if source not in self.sources:
            self.sources.append(source)

        try:
            self.data_dict[action][source]+=1
        except:
            if action not in self.data_dict:
                self.data_dict[action]={}
            self.data_dict[action][source]=1

    def select_3_most_popular(self):
        def count(action):
            return sum(self.data_dict[action].values())
        self.actions=sorted(self.actions,key=lambda x:count(x),reverse=True)[:3]

    def quantity_of_source(self,action):
        quantity=[]
        for i in self.sources:
            quantity.append(self.data_dict[action].get(i,0))
        return quantity

    def print_chart(self):
        self.select_3_most_popular()
        ind=range(1,len(self.sources)+1)
        x=plt.title("Chart three most popular actions by sources")
        plt.xticks(ind,self.sources, rotation='vertical')
        plt.margins(0.02)
        plt.subplots_adjust(bottom=0.45)
        #plt.yscale('log')

        p1=plt.bar(ind,self.quantity_of_source(self.actions[0]),color='red',width=0.85, align='center')
        p2=plt.bar(ind,self.quantity_of_source(self.actions[1]),color='green',width=0.85, align='center')
        p3=plt.bar(ind,self.quantity_of_source(self.actions[2]),color='blue',width=0.85, align='center')

        plt.legend((p1[0], p2[0],p3[0]), self.actions)
        plt.ylim(0,1000000)#to change
        plt.savefig('Char_actions_by_source.jpg',dpi=300)
        plt.clf()
