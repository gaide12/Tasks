def max_odd(array):
    max=0
    for i in array:
        if isinstance(i,int|float) and i%2!=0 and i>max:
            max = int(i)
    if not max:
        max=None
    print(max)

max_odd([1, 2, 3, 4, 4]) # => 3
max_odd([21.0, 2, 3, 4, 4]) # => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu']) # => None
max_odd([2, 2, 4])