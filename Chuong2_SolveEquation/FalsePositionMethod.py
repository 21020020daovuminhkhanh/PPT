import math
from tabulate import tabulate

print("Giải phương trình bằng phương pháp Điểm sai")
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
start = input("Nhập p0 p1: ")
start = list(map(float, start.split()))
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

print("Phuơng trình của bạn là: g(x) =", expression)


def calc(k):
    namespace['x'] = k
    return eval(expression, namespace)


p0 = start[0]
p1 = start[1]
arr = [p0, p1]
c = [calc(p0), calc(p1)]

for i in range(2, n):
    q0 = calc(p0)
    q1 = calc(p1)

    p = p1 - q1 * (p1 - p0) / (q1 - q0)

    arr.append(p)
    c.append(calc(p))
    if abs(p - p1) < e:
        break

    q = calc(p)
    if q * q0 < 0:
        p0 = p1
        q0 = q1
    p1 = p
    q1 = q

data = [
    ['i', 'pi', 'f(pi)']
]
for i in range(len(arr)):
    data.append([i, arr[i], c[i]])

print(tabulate(data, headers="firstrow", floatfmt=".15f"))