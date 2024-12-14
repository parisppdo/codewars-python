def calculate_sum(N, K):
    divider = K
    total_sum = 0
    cache = {}

    for count in range(1, N + 1):
        if (count % divider) != 0:
            total_sum += count
        else:
            key = count

            while count % K == 0:
                if count in cache:
                    count = cache[count]
                    break
                count = count // divider

            if key not in cache:
                cache[key] = count
            total_sum += count

    return total_sum

print(calculate_sum(10, 4))
print(calculate_sum(25, 9))
print(calculate_sum(66, 2))