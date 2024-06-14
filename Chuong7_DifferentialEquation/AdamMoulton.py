import math

import numpy as np
import sys
from tabulate import tabulate

print("Phương trình vi phân bằng phương pháp hiệu chỉnh Adam-Moulton")
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