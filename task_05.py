import datetime
def  date_in_future(integer=0):
    newdata = datetime.datetime.today()
    if isinstance(integer,int) and integer!=0:
        newdata+=datetime.timedelta(integer)
        return (f"{newdata.date()} {newdata.hour}:{newdata.minute}:{newdata.second}'")
    else:
        return (f"{newdata.date()} {newdata.hour}:{newdata.minute}:{newdata.second}'")
print(date_in_future(3)) # => текущая дата
print(date_in_future()) # => текущая дата + 2 дня