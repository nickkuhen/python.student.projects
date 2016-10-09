#Python version ........

from Tkinter import *
from datetime import datetime, timedelta
from pytz import timezone

now_pdx = datetime.now(timezone('US/Pacific'))
now_nyc = datetime.now(timezone('US/Eastern'))
now_lon = datetime.now(timezone('Europe/London'))
                                
print "The local time in Portland is", now_pdx.strftime("%H:%M:%S")

Portland = now_pdx.strftime('%H')
New_York = now_nyc.strftime('%H')
London = now_lon.strftime('%H')

#officeList = ['Portland', 'New.York', 'London']
#for x in officeList:
if 9 <= Portland >= 21:
    print ("Portland Office is open")
else:
    print("Portland Office is closed")
if 9 <= New_York >= 21:
    print ("New York Office is open")
else:
    print("New York Office is closed")
if 9 <= London >= 21:
    print ("London Office is open")
else:
    print("London Office is closed")

    



'''
nycopen = datetime.strptime('09:00:00', '%H:%M:%S')
nycclose = datetime.strptime('21:00:00', '%H:%M:%S')
nycopen += timedelta(hours=3)
nycclose += timedelta(hours=3)

if datetime.now() >= nycopen >= nycclose:
    

lonopen = datetime.strptime('09:00:00', '%H:%M:%S')
lonclose = datetime.strptime('21:00:00', '%H:%M:%S')
lonopen += timedelta(hours=8)
lonclose += timedelta(hours=8)

if datetime.now() >= lonopen >= lonclose:
    print ("London Office is open")
else:
    print("London Office is closed")

'''
