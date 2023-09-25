def approx_equals(a, b):
    a = round(a, 3)
    b = round(b, 3)
    err = 1e-3
    print (abs(a - b))
    if abs(a - b) < err:
        return True
    else:
        return False
approx_equals(123.2345, 123.234501)