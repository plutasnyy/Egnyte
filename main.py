from chart import *
from observer import *
from data import *

chart=First()
observer=Observer()
data=Data(observer)

observer.add_observer(chart)

data.read_data()
