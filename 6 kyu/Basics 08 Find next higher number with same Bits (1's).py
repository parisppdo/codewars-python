def next_higher(n):
    # Creating the left part of the asked number
    next_higher = n + (n & -n)
    
    # creating the right part of the asked number
    right_ones_pattern = n ^ next_higher
    right_ones_pattern = (right_ones_pattern // (n & -n)) >> 2
    
    # Adding the two, to create the final form
    return next_higher | right_ones_pattern

a = next_higher(128)
print(a)
