import math

import numpy as np
import sys
from tabulate import tabulate

print("Tính đạo hàm bằng công thức sai phân")
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
for i in range(0, N - 1):
    derivative.append((Y[i] - Y[i + 1]) / (X[i] - X[i + 1]))
derivative.append((Y[N - 1] - Y[N - 2]) / (X[N - 1] - X[N - 2]))


data = [
    ['x', 'f(x)', 'f\'(x)', 'Sai số']
]
for i in range(0, N):
    data.append([X[i], Y[i], derivative[i], abs(calc(X[i]) - derivative[i])])

print(tabulate(data, headers="firstrow", floatfmt=".10f"))

