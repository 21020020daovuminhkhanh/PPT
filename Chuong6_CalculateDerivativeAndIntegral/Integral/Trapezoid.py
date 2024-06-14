import math

import numpy as np
import sys
from tabulate import tabulate

print("Tính tích phân bằng công thức hình thang")
print("Nhập 2 cận tích phân: ")
lbound, ubound = list(map(float, input().split()))

N = int(input("Nhập số khoảng con N: "))
h = (ubound - lbound) / N

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
expression = input("Nhập hàm số cần tính tích phân: ")
expression2 = input("Nhập hàm số thực tế: ")


def calc(k, e):
    namespace['x'] = k
    return eval(e, namespace)


print("Kết quả là: ", end='')
ans = 0
for i in range(0, N + 1):
    if i == 0 or i == N:
        ans += calc(lbound + i * h, expression)
    else:
        ans += 2 * calc(lbound + i * h, expression)
ans = ans * h / 2
print(ans)
print("Sai số: " + str(abs(calc(ubound, expression2) - calc(lbound, expression2) - ans)))
