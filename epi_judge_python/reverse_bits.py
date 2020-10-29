from test_framework import generic_test


def reverse_bits(x: int) -> int:
    y = 0
    pos = 63
    while x:
        next_bit = x & 1
        y += next_bit << pos
        x >>= 1
        pos -= 1
    return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
