import math
from tabulate import tabulate

print("Giải phương trình bằng phương pháp chia đôi")
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
interval = input("Nhập khoảng tính toán: ")
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


interval = list(map(float, interval.split()))

print("Phuơng trình của bạn là: f(x) =", expression)


def calc(k):
    namespace['x'] = k
    return eval(expression, namespace)


a = interval[0]
b = interval[1]

print("f(" + str(a) + ") = " + str(calc(a)))
print("f(" + str(b) + ") = " + str(calc(b)))

arr = []
for i in range(n):
    p = (a + b) / 2
    arr.append(p)
    if len(arr) >= 2:
        if abs(arr[len(arr) - 1] - arr[len(arr) - 2]) < e:
            break
    if calc(p) == 0:
        break
    elif calc(a) * calc(p) < 0:
        b = p
    else:
        a = p


c = list(map(calc, arr))

data = [
    ['i', 'pi', 'f(pi)']
]
for i in range(len(arr)):
    data.append([i + 1, arr[i], c[i]])

print(tabulate(data, headers="firstrow", floatfmt=".10f"))
