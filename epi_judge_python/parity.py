from test_framework import generic_test


def parity(x: int) -> int:
    par = True
    while x:
        par = not par
        x = x & (x - 1)
    return 1 if not par else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
