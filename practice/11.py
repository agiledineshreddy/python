def print_rangoli(size):
    m = ord('a')
    width = 4 * size - 3
    for i in range(1, size + 1):
        r = []
        for k in range(1, i + 1):
            r.append(chr(m + size - k))
        print('-'.join(r + r[-2::-1]).center(width, '-'))
    for i in range(size - 1, 0, -1):
        r = []
        for k in range(1, i + 1):
            r.append(chr(m + size - k))
        print('-'.join(r + r[-2::-1]).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)