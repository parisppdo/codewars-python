def next_higher(n):
    
    # Converting the given number into its binary form
    bnr = bin(n)[2:]

    # Counting the ones of the binary number
    ones = bnr.count("1")

    # Finding the number using a While loop
    while True:
        n += 1
        ones2 = bin(n)[2:].count("1")
        if ones == ones2:
            break
    
    return n

a = next_higher(201326592)
print(a)
