def sort_list(list=[]):
    length = len(list)
    if length>1:
        n_list=sorted(list)
        min_el=n_list[0]
        max_el=n_list[length-1]
        for i in range(length):
            if list[i]==min_el:
                list[i]=max_el
            elif list[i]==max_el:
                list[i]=min_el
        list.append(min_el)
        print(list)
    elif length==1:
        list.append(list[0])
        print(list)
    else:
        print(list)


sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]

