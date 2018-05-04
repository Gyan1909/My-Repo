def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
