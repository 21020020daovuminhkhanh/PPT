import numpy as np
import sys

print("Tính trị riêng bằng phương pháp lặp nghịch đảo")
n = int(input("Nhập kích thước ma trận n: "))
matrix = []
print("Nhập ma trận: ")
for i in range(0, n):
    matrix.append(list(map(float, input().split())))
matrix = np.array(matrix)

x0 = list(map(float, input("Nhập vector khởi tạo: ").split()))
x0 = np.array(x0).transpose()
k = int(input("Nhập số vòng lặp k: "))


def gauss_elimination(m, b):
    n = len(m)
    for i in range(n):
        # Tìm phần tử lớn nhất trong cột dưới đường chéo
        max_row = i
        for k in range(i + 1, n):
            if abs(m[k][i]) > abs(m[max_row][i]):
                max_row = k

        # Hoán đổi hàng
        m[i], m[max_row] = m[max_row], m[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Biến đổi để tạo ma trận tam giác trên
        for k in range(i + 1, n):
            factor = m[k][i] / m[i][i]
            b[k] -= factor * b[i]
            for j in range(i, n):
                m[k][j] -= factor * m[i][j]
            # print(np.hstack((matrix, np.array([b]).transpose())))

    # Giải hệ phương trình tam giác trên
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if m[i][i] == 0 and b[i] == 0:
            print("Hệ vô số nghiệm")
            sys.exit()
        elif m[i][i] == 0 and b[i] != 0:
            print("Hệ vô nghiệm")
            sys.exit()
        x[i] = b[i] / m[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= m[k][i] * x[i]
    return x


ans = 0
temp = matrix.copy()
for i in range(0, k):
    y = gauss_elimination(temp, x0)
    ans = np.min(y)
    if np.max(np.abs(y)) == np.max(y):
        t = np.max(np.abs(y))
    else:
        t = -np.max(np.abs(y))
    x0 = y / t
    temp = matrix.copy()


print("Trị riêng nhỏ nhất của ma trận là:", 1/ans)