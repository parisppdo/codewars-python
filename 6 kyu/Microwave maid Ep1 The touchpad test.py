def get_best_combination(seconds):
    import itertools
    min1 = str(seconds // 60)
    sec1 = str(seconds % 60)
    min2 = str(int(min1) - 1)
    sec2 = str(seconds - int(min2) * 60)
    if len(sec1) == 1:
        sec1 = '0' + sec1
    if len(sec2) == 1:
        sec2 = '0' + sec2 
    method1 = min1 + sec1
    method2 = min2 + sec2
    method1 = method1.lstrip('0')
    method2 = method2.lstrip('0')
    smallMethod1 = ''.join(i for i, _ in itertools.groupby(method1))
    smallMethod2 = ''.join(i for i, _ in itertools.groupby(method2))
    if len(method1) > 4:
        return method2
    if len(method2) > 4:
        return method1
    if len(smallMethod1) > len(smallMethod2):
        return method2
    elif len(smallMethod1) < len(smallMethod2):
        return method1
    else:
        if len(method1) > len(method2):
            return method2
        if len(method1) < len(method2):
            return method1
        else:
            return method1