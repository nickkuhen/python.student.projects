#Python version ........

from Tkinter import *
from datetime import datetime, timedelta
from pytz import timezone


now_pdx = datetime.now(timezone('US/Pacific'))
print "The local time in Portland is", now_pdx.strftime("%H:%M:%S")

pdxopen = datetime.strptime("09:00:00", '%H:%M:%S')
pdxclose = datetime.strptime('21:00:00', '%H:%M:%S')

if datetime.now() >= pdxopen > pdxclose:
    print ("Portland Office is open")
else:
    print("Portland Office is closed")

nycopen = datetime.strptime('09:00:00', '%H:%M:%S')
nycclose = datetime.strptime('21:00:00', '%H:%M:%S')
nycopen += timedelta(hours=3)
nycclose += timedelta(hours=3)

if datetime.now() >= nycopen > nycclose:
    print ("New York Office is open")
else:
    print("New York Office is closed")

lonopen = datetime.strptime('09:00:00', '%H:%M:%S')
lonclose = datetime.strptime('21:00:00', '%H:%M:%S')
lonopen += timedelta(hours=8)
lonclose += timedelta(hours=8)

if datetime.now() >= lonopen > lonclose:
    print ("London Office is open")
else:
    print("London Office is closed")
