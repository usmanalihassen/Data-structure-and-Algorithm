def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(' ' * (rows - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

# Number of rows for the pyramid
n = 5
print_pyramid(n)
