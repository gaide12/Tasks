import operator
def connect_dicts(dict1, dict2):
 connected={}
 for key,value in dict1.items():
     if value>10:
         connected.update({key:value})
 for key,value in dict2.items():
     dict2[key]
     if value>10:
        if key in dict1:
            if  sum(dict1.values()) <= sum(dict2.values()):
                connected.update({key: value})
        else: connected.update({key:value})

 sorted_dict=sorted(connected.items(),key=operator.itemgetter(1))
 return dict(sorted_dict)

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # =>
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))
print(operator.itemgetter(1))
