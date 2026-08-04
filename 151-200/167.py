def max(*args):
    if not args:
        raise ValueError()

    for i in args:
        if type(i) != int:
            raise ValueError()

    result = args[0]
    for i in args:
        if i > result:
            result = i

    return result
