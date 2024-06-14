import math
from tabulate import tabulate
import sympy as sp

print("Giải phương trình bằng phương pháp Newton")
x = 0

# Define the namespace with the math functions and variables
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

# Get the mathematical expression from the user
expression = input("Nhập hàm số: ")
start = input("Nhập p0: ")
start = float(start)

n = input("Nhập số vòng lặp: ")
if n.strip() == '':
    n = 100
    print("100 vòng lặp")
n = int(n)

e = input("Nhập điều kiện dừng: ")
if e.strip() == '':
    e = 0.0001
    print("Điều kiện dừng |pi - pi+1| <", e)
e = float(e)

print("Phuơng trình của bạn là: f(x) =", expression)


def calc(k):
    namespace['x'] = k
    return eval(expression, namespace)


p0 = start
p = 0
arr = [p0]
c = [calc(p0)]
for i in range(n):
    derivative = sp.diff(expression, 'x')
    p = p0 - calc(p0) / derivative.subs('x', p0)
    arr.append(p)
    c.append(calc(p))
    if abs(p - p0) < e:
        break
    p0 = p

x**2 - 6
data = [
    ['i', 'pi', 'f(pi)']
]
for i in range(len(arr)):
    data.append([i, arr[i], c[i]])

print(tabulate(data, headers="firstrow", floatfmt=".20f"))
