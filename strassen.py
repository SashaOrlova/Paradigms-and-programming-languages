import numpy as np


def read_arrays(n):
    new_array = power_of_two(n)
    for i in range(n):
        new_array[i, :n] = np.asarray(input().split(), dtype=int)
    return new_array


def power_of_two(n):
    m = 1
    while m < n:
        m *= 2
    return np.zeros((m, m), dtype=int)


def split(m):
    upper, lower = np.vsplit(m, 2)
    return np.hsplit(upper, 2) + np.hsplit(lower, 2)


def strassen(a, b):
    if a.size == 1:
        return np.array(a * b)
    else:
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)
        p1 = strassen(a11 + a22, b11 + b22)
        p2 = strassen(a21 + a22, b11)
        p3 = strassen(a11, b12 - b22)
        p4 = strassen(a22, b21 - b11)
        p5 = strassen(a11 + a12, b22)
        p6 = strassen(a21 - a11, b11 + b12)
        p7 = strassen(a12 - a22, b21 + b22)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 + p3 - p2 + p6
        c1 = np.hstack((c11, c12))
        c2 = np.hstack((c21, c22))
        return np.vstack((c1, c2))


def print_array(a):
        for row in a:
            print(*row)


if __name__ == "__main__":
    n = int(input())
    a = read_arrays(n)
    b = read_arrays(n)
    new_array = strassen(a, b)
    print_array(new_array[:n, :n])
