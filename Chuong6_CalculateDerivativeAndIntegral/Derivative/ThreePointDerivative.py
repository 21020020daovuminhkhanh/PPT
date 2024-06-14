import math

import numpy as np
import sys
from tabulate import tabulate

print("Tính đạo hàm bằng công thức ba điểm")
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
    if i == 0:
        derivative.append((-3 * Y[0] + 4 * Y[1] - Y[2]) / (2 * (X[1] - X[0])))
    elif i == N - 1:
        derivative.append((-3 * Y[N - 1] + 4 * Y[N - 2] - Y[N - 3]) / (2 * (X[0] - X[1])))
    else:
        derivative.append((Y[i + 1] - Y[i - 1]) / (2 * (X[1] - X[0])))

data = [
    ['x', 'f(x)', 'f\'(x)', 'Sai số']
]
for i in range(0, N):
    data.append([X[i], Y[i], derivative[i], abs(calc(X[i]) - derivative[i])])

print(tabulate(data, headers="firstrow", floatfmt=".10f"))