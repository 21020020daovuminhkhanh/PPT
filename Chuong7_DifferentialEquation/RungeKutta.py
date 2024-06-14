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


x0temp, y0temp = x0, y0
# Runge-Kutta bậc ba
X = [x0]
Y = [y0]
while x0 < b:
    k1 = calc(x0, y0, expression)
    k2 = calc(x0 + h/2, y0 + 0.5 * k1 * h, expression)
    k3 = calc(x0 + h, y0 - k1 * h + 2 * k2 * h, expression)
    y0 = y0 + h / 6 * (k1 + 4 * k2 + k3)
    Y.append(y0)
    x0 += h
    X.append(x0)

data = [
    ['i', 'xi', 'yi', 'Giá trị thực tế', 'Sai số']
]
for i in range(len(X)):
    trueVal = calc(X[i], Y[i], expression2)
    data.append([i, X[i], Y[i], trueVal, abs(trueVal - Y[i])])

print("Kết quả phương pháp Runge-Kutta bậc ba: ")
print(tabulate(data, headers="firstrow", floatfmt=".10f"))
print()


x0, y0 = x0temp, y0temp
# Runge-Kutta bậc bốn
X = [x0]
Y = [y0]
while x0 < b:
    k1 = calc(x0, y0, expression)
    k2 = calc(x0 + h / 2, y0 + 0.5 * k1 * h, expression)
    k3 = calc(x0 + h / 2, y0 + 0.5 * k2 * h, expression)
    k4 = calc(x0 + h, y0 + k3 * h, expression)
    y0 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    Y.append(y0)
    x0 += h
    X.append(x0)

data = [
    ['i', 'xi', 'yi', 'Giá trị thực tế', 'Sai số']
]
for i in range(len(X)):
    trueVal = calc(X[i], Y[i], expression2)
    data.append([i, X[i], Y[i], trueVal, abs(trueVal - Y[i])])

print("Kết quả phương pháp Runge-Kutta bậc bốn: ")
print(tabulate(data, headers="firstrow", floatfmt=".10f"))
