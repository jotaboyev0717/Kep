def filter_list(a, b):
    if b != 0:
        return [i for i in a if i % 2 == 0]
    else:
        return [i for i in a if i % 2 == 1]