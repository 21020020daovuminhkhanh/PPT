print("Nội suy Newton")
n = int(input("Nhập số điểm mốc n: "))
print("Nhập các mốc: ")
arr = []
for i in range(0, n):
    x = list(map(float, input().split()))
    arr.append(x)

print("Nhập mốc cần tính toán: ")
x = float(input())
ans = 0