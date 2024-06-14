import math

import numpy as np
import sys

print("Xấp xỉ bình phương tối thiểu rời rạc")
N = int(input("Nhập số điểm mốc N: "))
print("Nhập các mốc: ")

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print("Nhập bậc của đa thức xấp xỉ: ")
deg = int(input())

print("Nhập mốc cần tính toán: ")
x = float(input())


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


X = np.array(X)
Y = np.array(Y)
X1 = np.sum(X)
X2 = np.sum(np.power(X, 2))
X3 = np.sum(np.power(X, 3))
X4 = np.sum(np.power(X, 4))
X5 = np.sum(np.power(X, 5))
X6 = np.sum(np.power(X, 6))
XY = np.sum(X * Y)
X2Y = np.sum(np.power(X, 2) * Y)
X3Y = np.sum(np.power(X, 3) * Y)


# Xấp xỉ bình phương tối thiểu bậc nhất
A1 = [[N, X1], [X1, X2]]
b1 = [np.sum(Y), XY]
result1 = gauss_elimination(A1, b1)
E1 = 0
for i in range(0, N):
    E1 += (result1[0] + result1[1] * X[i] - Y[i]) ** 2
print("Xấp xỉ tuyến tính của bộ dữ liệu là đa thức:")
print("y = " + str(result1[1]) + "x + " + str(result1[0]))
print("Sai số:", str(E1))
print()


# Xấp xỉ bình phương tối thiểu bậc hai
A2 = [[N, X1, X2], [X1, X2, X3], [X2, X3, X4]]
b2 = [np.sum(Y), XY, X2Y]
result2 = gauss_elimination(A2, b2)
E2 = 0
for i in range(0, N):
    E2 += (result2[0] + result2[1] * X[i] + result2[2] * X[i] * X[i] - Y[i]) ** 2
print("Xấp xỉ bậc hai của bộ dữ liệu là đa thức:")
print("y = " + str(result2[2]) + "x^2 + " + str(result2[1]) + "x + " + str(result2[0]))
print("Sai số:", str(E2))
print()


# Xấp xỉ bình phương tối thiểu bậc ba
A3 = [[N, X1, X2, X3], [X1, X2, X3, X4], [X2, X3, X4, X5], [X3, X4, X5, X6]]
b3 = [np.sum(Y), XY, X2Y, X3Y]
result3 = gauss_elimination(A3, b3)
E3 = 0
for i in range(0, N):
    E3 += (result3[0] + result3[1] * X[i] + result3[2] * X[i] * X[i] + result3[3] * (X[i]**3) - Y[i]) ** 2
print("Xấp xỉ bậc ba của bộ dữ liệu là đa thức:")
print("y = " + str(result3[3]) + "x^3 + " + str(result3[2]) + "x^2 + " + str(result3[1]) + "x + " + str(result3[0]))
print("Sai số:", str(E3))
print()


# Xấp xỉ hàm mũ
lnY = np.log(Y)
XlnY = np.sum(X * lnY)
A4 = [[N, X1], [X1, X2]]
b4 = [np.sum(lnY), XlnY]
result4 = gauss_elimination(A4, b4)
E4 = 0
for i in range(0, N):
    E4 += (math.e ** (result4[1] * X[i] + result4[0]) - Y[i]) ** 2
print("Xấp xỉ hàm mũ của bộ dữ liệu có phương trình:")
print("y = " + str(math.e ** result4[0]) + "e^" + str(result4[1]) + "x")
print("Sai số:", str(E4))
print()


# Xấp xỉ hàm lũy thừa
lnX = np.log(X)
lnX2 = np.sum(np.power(lnX, 2))
lnXlnY = np.sum(lnX * lnY)
A5 = [[N, np.sum(lnX)], [np.sum(lnX), lnX2]]
b5 = [np.sum(lnY), lnXlnY]
result4 = gauss_elimination(A5, b5)
E5 = 0
for i in range(0, N):
    E5 += (X[i] ** result4[1] * math.e ** result4[0] - Y[i]) ** 2
print("Xấp xỉ hàm lũy thừa của bộ dữ liệu có phương trình:")
print("y = " + str(math.e ** result4[0]) + "x^" + str(result4[1]))
print("Sai số:", str(E5))