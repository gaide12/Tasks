def coincidence(list=None,range=None):
    outlist = []
    if list==None or range==None:
        return (outlist)
    else:
        for i in list:
            if isinstance(i,int|float):
                if int(i) in range:
                    outlist.append(i)
        return (outlist)
print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]
