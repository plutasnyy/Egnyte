from chart_quantity_of_actions import *
from chart_quantity_of_actions_with_source import *
from chart_actions_most_activity_group import *

from observer import *
from data import *

def add_charts(charts_list):
    charts_list.append(Quantity_of_actions())
    charts_list.append(Quantity_of_actions_with_source())
    charts_list.append(Actions_of_most_activity_group())

def add_observers(charts_list,observer):
    for chart in charts_list:
        observer.add_observer(chart)

charts_list=[]

observer=Observer()
data=Data(observer)

add_charts(charts_list)
add_observers(charts_list,observer)

data.read_data()
