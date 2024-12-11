def calculate_sum(N, K):

    divisible = []
    non_divisible = []
    divider = K

    for i in range (1, N + 1):
        if (i % K) != 0:
            non_divisible.append(i)
        else:
            while i % K == 0:
                divisible.append(i)
                i = i // divider

    divisible_sum = sum(divisible)
    non_divisible_sum = sum(non_divisible)

    return divisible_sum + non_divisible_sum

print(calculate_sum(16, 2))