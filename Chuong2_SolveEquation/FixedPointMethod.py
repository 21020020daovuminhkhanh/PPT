import math
from tabulate import tabulate

print("Giải phương trình bằng phương pháp Điểm bất động")
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


print("Phuơng trình của bạn là: g(x) =", expression)


def calc(k):
    namespace['x'] = k
    return eval(expression, namespace)


arr = [calc(start)]
c = [calc(start) - calc(calc(start))]

for i in range(n):
    p = calc(arr[len(arr) - 1])
    arr.append(p)
    c.append(p - calc(p))
    if abs(p - arr[len(arr) - 2]) < e:
        break


data = [
    ['i', 'pi', 'pi - g(pi)'],
    [0, start, start - calc(start)]
]
for i in range(len(arr)):
    data.append([i + 1, arr[i], c[i]])

print(tabulate(data, headers="firstrow", floatfmt=".10f"))
