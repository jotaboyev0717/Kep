def argv_int(*args):
    s = 0
    for i in args:
        if type(i) == int:
            s +=1
    return s