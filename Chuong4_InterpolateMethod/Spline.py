import sys

print("Nội suy Spline")
N = int(input("Nhập số điểm mốc N: "))
print("Nhập các mốc: ")

X = list(map(float, input().split()))
Y = list(map(float, input().split()))


print("Nhập đạo hàm tại điểm mốc đầu và cuối alpha, beta: ")
alpha, beta = map(float, input().split())

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


# Tính hi = xi+1 - xi, fi = yi+1 - yi
H = []
F = []
for i in range(0, N-1):
    H.append(X[i + 1] - X[i])
    F.append(Y[i + 1] - Y[i])

A = []
for i in range(0, N):
    k = [float(0) for j in range(0, N)]
    if i == 0:
        k[0] = 2/3 * H[0]
        k[1] = 1/3 * H[0]
    elif i == N - 1:
        k[N - 2] = 1/3 * H[N - 2]
        k[N - 1] = 2/3 * H[N - 2]
    else:
        k[i - 1] = 1/3 * H[i - 1]
        k[i] = 2/3 * (H[i - 1] + H[i])
        k[i + 1] = 1/3 * H[i]
    A.append(k)

b = []
for i in range(0, N):
    if i == 0:
        b.append(round(F[0]/H[0] - alpha, 10))
    elif i == N - 1:
        b.append(round(beta - F[N - 2]/H[N - 2], 10))
    else:
        b.append(round(F[i]/H[i] - F[i - 1]/H[i - 1], 10))


Bi = gauss_elimination(A, b)
Ai = []
Ci = []
Di = []
for i in range(0, N - 1):
    Ai.append(round(1/3 * (Bi[i + 1] - Bi[i]) / H[i], 10))
    Ci.append(round(F[i]/H[i] - 1/3 * (Bi[i + 1] + 2 * Bi[i]) * H[i], 10))
    Di.append(Y[i])

Bi.pop()
print("ai =", Ai)
print("bi =", Bi)
print("ci =", Ci)
print("di =", Di)

for i in range(0, N):
    if x < X[i]:
        ans = Ai[i - 1] * (x - X[i - 1])**3 + Bi[i - 1] * (x - X[i - 1])**2 + Ci[i - 1] * (x - X[i - 1]) + Di[i - 1]
        print("Kết quả nội suy Spline tại x = " + str(x) + " là: " + str(round(ans, 10)))
        break
