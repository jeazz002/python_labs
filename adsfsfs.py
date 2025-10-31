a = int(input())
n = 0
b = 0
counter = 0
flag = "YES"
while a != 0:
    c = b
    b = a % 10
    if b <= c:
        counter += 1
    a = a//10
if counter >= 0:
    print("NO")
else:
    print("YES")
    