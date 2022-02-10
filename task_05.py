import datetime
def  date_in_future(integer=0):
    newdata = datetime.datetime.today()
    if isinstance(integer,int) and integer!=0:
        newdata+=datetime.timedelta(integer)
        print(f"{newdata.date()} {newdata.hour}:{newdata.minute}:{newdata.second}'")
    else:
        print(f"{newdata.date()} {newdata.hour}:{newdata.minute}:{newdata.second}'")
date_in_future([]) # => текущая дата
date_in_future() # => текущая дата + 2 дня