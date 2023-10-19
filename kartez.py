def tpl_sort(a):
    for z in a:
        if not isinstance(z, int):
            return ()
    return tuple(sorted(a))
print(tpl_sort((6, 10, 5, 2, 7)))
print(tpl_sort((8, 5, 1.5, 3, 12)))