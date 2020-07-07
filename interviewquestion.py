# given a dictonary d where key is of form yyyy-mm-dd and its corresponding value is an integer, return a new dictionary D with missing dates values which are average of prev and next value
from datetime import date

import datetime
from collections import OrderedDict


def numOfDays(date1, date2):
    date1=list(date1.split("-"))
    date2=list(date2.split("-"))
    date1=list(map(lambda x:int(x),date1))
    date2=list(map(lambda x:int(x),date2))
    date1=date(date1[0],date1[1],date1[2])
    date2=date(date2[0],date2[1],date2[2])
    return (date2-date1).days


def next_date(d):
    d=list(d.split("-"))
    d=list(map(lambda x:int(x),d))
    d=date(d[0],d[1],d[2])+datetime.timedelta(days=1)
    s=""
    if (d.month//100==0):
        month="0"+str(d.month)
    else:
        month=str(d.month)

    if(d.day//100==0):
        day="0"+str(d.day)
    else:
        day=str(d.day)

    s+=str(d.year)+"-"+str(month)+"-"+str(day)
    return s
mydict={"2019-01-01":100,"2019-01-04":115}
ordered = OrderedDict(sorted(mydict.items(), key=lambda t: t[0]))

l=list(ordered.keys())
for i in range(1,len(l)):
    days=numOfDays(l[i-1],l[i])
    value=ordered[l[i]]-ordered[l[i-1]]
    interval=value//days
    a=ordered[l[i-1]]
    initial_date=l[i-1]
    for i in range(days-1):
        a+=interval
        ordered[next_date(initial_date)]=a
        initial_date=next_date(initial_date)

ordered = dict(OrderedDict(sorted(ordered.items(), key=lambda t: t[0])))
print(ordered)
