import math

import numpy as np
import sys
from tabulate import tabulate

print("Phương trình vi phân bằng phương pháp Điểm giữa")
x = 0
y = 0
namespace = {
    'cos': math.cos,
    'sin': math.sin,
    'tan': math.tan,
    'log': math.log,
    'log10': math.log10,
    'x': x,
    'y': y,
    'e': math.e,
    'pi': math.pi,
    'sqrt': math.sqrt
}
expression = input("Nhập phương trình vi phân: ")
expression2 = input("Nhập phương trình nghiệm thực tế: ")
h = float(input("Nhập bước nhảy h: "))
a, b = list(map(float, input("Nhập khoảng tính toán: ").split()))
x0, y0 = list(map(float, input("Nhập giá trị x0, y0: ").split()))


def calc(k, l, e):
    namespace['x'] = k
    namespace['y'] = l
    return eval(e, namespace)


X = [x0]
Y = [y0]
while x0 < b:
    f = calc(x0, y0, expression)
    xMid = x0 + h / 2
    yMid = y0 + h / 2 * f
    y0 = y0 + h * calc(xMid, yMid, expression)
    Y.append(y0)
    x0 += h
    X.append(x0)

data = [
    ['i', 'xi', 'yi', 'Giá trị thực tế', 'Sai số']
]
for i in range(len(X)):
    trueVal = calc(X[i], Y[i], expression2)
    data.append([i, X[i], Y[i], trueVal, abs(trueVal - Y[i])])

print(tabulate(data, headers="firstrow", floatfmt=".10f"))
