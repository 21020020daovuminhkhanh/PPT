import math

import numpy as np
import sys
from tabulate import tabulate

print("Tính đạo hàm bằng công thức 5 điểm")
N = int(input("Nhập số điểm mốc N: "))
print("Nhập các mốc: ")

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

x = 0
namespace = {
    'cos': math.cos,
    'sin': math.sin,
    'tan': math.tan,
    'log': math.log,
    'log10': math.log10,
    'x': x,
    'e': math.e,
    'pi': math.pi,
    'sqrt': math.sqrt
}
expression = input("Nhập hàm số thực tế: ")


def calc(k):
    namespace['x'] = k
    return eval(expression, namespace)


derivative = []
for i in range(0, N):
    if i == 0 or i == 1:
        derivative.append((-25 * Y[i] + 48 * Y[i + 1] - 36 * Y[i + 2] + 16 * Y[i + 3] - 3 * Y[i + 4]) / (12 * (X[1] - X[0])))
    elif i == N - 1 or i == N - 2:
        derivative.append((-25 * Y[i] + 48 * Y[i - 1] - 36 * Y[i - 2] + 16 * Y[i - 3] - 3 * Y[i - 4]) / (12 * (X[0] - X[1])))
    else:
        derivative.append((Y[i - 2] - 8 * Y[i - 1] + 8 * Y[i + 1] - Y[i + 2]) / (12 * (X[1] - X[0])))

data = [
    ['x', 'f(x)', 'f\'(x)', 'Sai số']
]
for i in range(0, N):
    data.append([X[i], Y[i], derivative[i], abs(calc(X[i]) - derivative[i])])

print(tabulate(data, headers="firstrow", floatfmt=".10f"))