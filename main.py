from chart import *
from observer import *
from data import *

def add_charts(charts_list):
    charts_list.append(First())

def add_observers(charts_list,observer):
    for chart in charts_list:
        observer.add_observer(chart)

charts_list=[]

observer=Observer()
data=Data(observer)

add_charts(charts_list)
add_observers(charts_list,observer)

data.read_data()
