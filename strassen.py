import numpy as np


def read_arrays(n):
    a = np.empty((n, n), dtype=int)
    b = np.empty((n, n), dtype=int)
    for i in range(n):
        a[i] = np.asarray(input().split(), dtype=int)
    for i in range(n):
        b[i] = np.asarray(input().split(), dtype=int)
    a0, b0, m = template(a, b, n)
    a = np.hstack((a, a0))
    b = np.hstack((b, a0))
    a = np.vstack((a, b0))
    b = np.vstack((b, b0))
    return a, b, m


def template(a, b, n):
    m = 1
    while m < n:
        m = m * 2
    a = np.zeros((n, m-n), dtype=int)
    b = np.zeros((m-n, m), dtype=int)
    return a, b, m


def split(m):
    a, b = np.vsplit(m, 2)
    a, c = np.hsplit(a, 2)
    b, d = np.hsplit(b, 2)
    return a, b, c, d


def strassen(a, b, q):
    if q == 1:
        d = np.array(a[0][0] * b[0][0])
        return d
    else:
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)
        p1 = strassen(a11 + a22, b11 + b22, q // 2)
        p2 = strassen(a21 + a22, b11, q // 2)
        p3 = strassen(a11, b12 - b22, q // 2)
        p4 = strassen(a22, b21 - b11, q // 2)
        p5 = strassen(a11 + a12, b22, q // 2)
        p6 = strassen(a21 - a11, b11 + b12, q // 2)
        p7 = strassen(a12 - a22, b21 + b22, q // 2)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 + p3 - p2 + p6
        c1 = np.hstack((c11, c12))
        c2 = np.hstack((c21, c22))
        c = np.vstack((c1, c2))
    return c


def print_array(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j], ' ', end='')
        print()

if __name__ == "__main__":
    n = int(input())
    a, b, q = read_arrays(n)
    a = strassen(a, b, q)
    print_array(a, n)
