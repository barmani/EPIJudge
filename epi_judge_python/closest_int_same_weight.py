from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    # weight = get_weight(x)
    # y = x + 1
    # z = x - 1
    # while True:
    #     if get_weight(y) == weight:
    #         return y
    #     elif get_weight(z) == weight:
    #         return z
    #     y += 1
    #     z -= 1
    # return 0
    for i in range(63):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            return x ^ ((1 << i) | (1 << (i + 1)))
    return 0


def get_weight(y):
    weight = 0
    while y:
        weight += 1 if y & 1 else 0
        y >>= 1
    return weight


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
