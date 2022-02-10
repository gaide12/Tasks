def coincidence(list=None,range=None):
    outlist = []
    if list==None or range==None:
        print (outlist)
    else:
        for i in list:
            if isinstance(i,int|float):
                if int(i) in range:
                    outlist.append(i)
        print(outlist)
coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
coincidence() # => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]
