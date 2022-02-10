
def multiply_numbers(inputs=None):
        b=1
        if inputs==None:
            print(inputs)
        elif isinstance(inputs, list):
            for i in range(len(inputs)):
                b *= inputs[i]
            print(b)
        else:
            if not isinstance(inputs,str):
                inputs=str(inputs)
            for i in range(len(inputs)):
                if '/'<inputs[i]<':':
                 b*=int(inputs[i])
            if b==1:
                b=None
            print(b)

multiply_numbers() # => None
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120