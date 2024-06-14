import math
import numpy as np
import sys

print("Giải hệ phương trình bằng phép khử Gauss")
n = int(input("Nhập số phương trình n: "))
A = []
print("Nhập ma trận hệ số A: ")
for i in range(n):
    A.append(list(map(int, input().split())))

print("Nhập hệ số tự do: ")
b = list(map(int, input().split()))


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


print("Hệ phương trình của bạn là: ")
Ab = np.hstack((A, np.array([b]).transpose()))
print(Ab)


def gauss_elimination(matrix, b):
    n = len(matrix)
    for i in range(n):
        # Tìm phần tử lớn nhất trong cột dưới đường chéo
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Hoán đổi hàng
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Biến đổi để tạo ma trận tam giác trên
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            b[k] -= factor * b[i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            # print(np.hstack((matrix, np.array([b]).transpose())))

    # Giải hệ phương trình tam giác trên
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if matrix[i][i] == 0 and b[i] == 0:
            print("Hệ vô số nghiệm")
            sys.exit()
        elif matrix[i][i] == 0 and b[i] != 0:
            print("Hệ vô nghiệm")
            sys.exit()
        x[i] = b[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= matrix[k][i] * x[i]
    return x


x = gauss_elimination(A, b)
print("Nghiệm của hệ phương trình là:", x)

