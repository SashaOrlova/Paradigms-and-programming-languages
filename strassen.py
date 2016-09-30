import numpy as np


def read_array(n):
    array = np.zeros((round(n), round(n)), dtype=int)
    for i in range(n):
        array[i, :n] = np.array(input().split(), dtype=int)
    return array


def round(n):
    n_extended = 1
    while n_extended < n:
        n_extended *= 2
    return n_extended


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
        c_upper = np.hstack((c11, c12))
        c_lower = np.hstack((c21, c22))
        return np.vstack((c_upper, c_lower))


def print_array(a):
    for row in a:
        print(*row)


if __name__ == "__main__":
    n = int(input())
    a = read_array(n)
    b = read_array(n)
    result = strassen(a, b)
    print_array(result[:n, :n])
