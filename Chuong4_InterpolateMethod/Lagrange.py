print("Nội suy Lagrange")
n = int(input("Nhập số điểm mốc n: "))
print("Nhập các mốc: ")
arr = []
for i in range(0, n):
    x = list(map(float, input().split()))
    arr.append(x)

print("Nhập mốc cần tính toán: ")
x = float(input())
ans = 0
for i in range(0, n):
    p = arr[i][1]
    for j in range(0, n):
        if j != i:
            p = p * (x - arr[j][0])
            p = p / (arr[i][0] - arr[j][0])
    ans += p

print("Dự đoán f(" + str(x) + ") =", ans)
t = float(input("Nhập giá trị thực: "))
print("Sai số là:", abs(ans - t))