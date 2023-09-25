def same_case(a, b): 
    if (not a.isalpha()) or (not b.isalpha()):
        return -1
    elif (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    else:
        return 0