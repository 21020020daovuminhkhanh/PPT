import math
import numpy as np
import sys

print("Giải hệ phương trình bằng phép lặp Gauss-Seidel")
n = int(input("Nhập số phương trình n: "))
A = []
print("Nhập ma trận hệ số A: ")
for i in range(n):
    A.append(list(map(int, input().split())))

print("Nhập hệ số tự do: ")
b = list(map(int, input().split()))

A = np.array(A)
b = np.array([b]).transpose()

print("Hệ phương trình của bạn là: ")
print(np.hstack((A, b)))

N = input("Nhập số vòng lặp: ")
if N.strip() == '':
    N = 100
    print("100 vòng lặp")
N = int(N)

e = input("Nhập điều kiện dừng: ")
if e.strip() == '':
    e = 0.0001
    print("Điều kiện dừng |pi - pi+1| <", e)
e = float(e)

A = A.astype(float)
b = b.astype(float)
for i in range(0, n):
    b[i] = b[i] / A[i][i]
    A[i] = A[i] / A[i][i]

U = np.triu(A, 1)
L = np.tril(A, -1)
I = np.eye(n)

C = (-1 * np.linalg.inv(np.add(I, L))) @ U
d = np.linalg.inv(np.add(I, L)) @ b

print("Nhập vecto x0: ")
x0 = list(map(int, input().split()))
x0 = np.array([x0]).transpose()

np.set_printoptions(precision=10)
for i in range(0, N):
    x = np.add(np.dot(C, x0), d)
    if np.linalg.norm(np.subtract(x, x0)) < e:
        break
    x0 = x
    print("x" + str(i + 1) + ":", x0.transpose())

print("Nghiệm của phương trình là:", x0.transpose())
