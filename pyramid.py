#pyramid pattern
def pyramid_pattern(row):
    for i in range(1, row + 1):
        print(' ' * (row - i) + '*' * (2 * i - 1))
pyramid_pattern(5)