from chart_abstract import *
import matplotlib.pyplot as plt

class Actions_of_most_activity_group(Chart):

    def __init__(self):
        self.data_dict={}
        self.actions=[]
        self.groups=[]

    def update(self,new_line):
        action=new_line['eventBody']['action']
        group=new_line['eventHeader']['workgroupID']
        self.data_dict[action]=self.data_dict.get(action,0)+1

        if group not in self.groups:
            self.groups.append(group)
        if action not in self.actions:
            self.actions.append(action)

        try:
            self.data_dict[group][action]+=1
        except:
            if group not in self.data_dict:
                self.data_dict[group]={}
            self.data_dict[group][action]=1

    def select_most_popular(self,number):
        def count(group):
            return sum(self.data_dict[group].values())
        self.groups=sorted(self.groups,key=lambda x:count(x),reverse=True)[:number]

    def print_chart(self):
        self.select_most_popular(1)
        data=sorted(self.data_dict[self.groups[0]].items(), key=lambda x: x[1])

        X=[i for i,k in data]
        Y=[k for i,k in data]
        ind=range(1,len(X)+1)

        plt.title("Actions of the most popular workgroup\nID: {}".format(self.groups[0]))
        plt.bar(ind,Y,width=0.85, align='center')
        plt.xticks(ind, X, rotation='vertical')
        plt.margins(0.015)
        plt.subplots_adjust(bottom=0.42)
        plt.yscale('log')
        plt.ylim(0,max(Y)*3)

        for x,y in zip(ind,Y):
            plt.text(x,y*1.5,y,ha='center',size='xx-small')

        plt.savefig('Actions of most popular group.jpg',dpi=300)
        plt.clf()
