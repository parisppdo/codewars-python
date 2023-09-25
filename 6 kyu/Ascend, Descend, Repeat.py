def ascend_descend(length, minimum, maximum):
    string = ''
    if maximum < minimum or length == 0:
        return string
    elif minimum == maximum:
        return string.ljust(length, str(maximum))
    else:
        for i in range(minimum, maximum):
            string +=str(i) 
        for i in range(maximum, minimum, -1):
            string +=str(i)
        string = length * string
    return string[0 : length]