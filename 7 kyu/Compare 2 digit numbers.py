def compare(a, b):
    a = str(a)
    b = str(b)
    if (a[0] == b[0] or a[0] == b[1]) and (a[1] == b[0] or a[1] == b[1]):
        if a[0] == a[1] and b[0] == b[1]:
            return '100%'
        elif a[0] == a[1] or b[0] == b[1]:
            return '50%'
        else:
            return '100%'
    if a[0] != b[0] and a[0] != b[1] and a[1] != b[0] and a[1] != b[1]:
        return '0%'
    if a[0] == b[0] or a[0] == b[1] or a[1] == b[0] or a[1] == b[1]:
        return '50%'