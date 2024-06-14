import numpy as np

print("Tính trị riêng bằng phương pháp lũy thừa")
n = int(input("Nhập kích thước ma trận n: "))
matrix = []
print("Nhập ma trận: ")
for i in range(0, n):
    matrix.append(list(map(float, input().split())))
matrix = np.array(matrix)

x0 = list(map(float, input("Nhập vector khởi tạo: ").split()))
x0 = np.array(x0).transpose()
k = int(input("Nhập số vòng lặp k: "))

ans = 0
for i in range(0, k):
    y = np.dot(matrix, x0)
    ans = np.max(y)
    x0 = y / abs(np.amax(y))

print("Trị riêng lớn nhất của ma trận là:", ans)