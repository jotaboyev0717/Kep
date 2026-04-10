def even_index_or_value(a):
    return [a[i] for i in range(len(a)) if i % 2 == 0 or a[i] % 2 == 0]