def calculate_sum(N, K):
    divisible = []
    non_divisible = []
    divider = K

    for count in range(1, N + 1):
        if (count % divider) != 0:
            non_divisible.append(count)
        else:
            while count % K == 0:
                count = count // divider
            divisible.append(count)

    divisible_sum = sum(divisible)
    non_divisible_sum = sum(non_divisible)

    return divisible_sum + non_divisible_sum

