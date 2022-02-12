
def multiply_numbers(inputs=None):
    b=1
    if inputs==None:
        return inputs
    elif isinstance(inputs, list):
        for i in range(len(inputs)):
            b *= inputs[i]
        return b
    else:
        if not isinstance(inputs,str):
            inputs=str(inputs)
        for i in range(len(inputs)):
            if '/'<inputs[i]<':':
                 b*=int(inputs[i])
        if b==1:
            b=None
        return b

print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120