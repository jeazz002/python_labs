s = input()
if len(s) % 2 != 0:
    a = s[:len(s)//2+1]
    b = s[len(a):]
    print(b+a)
else:
    a = s[:len(s)//2+1]
    b = s[len(a):]
    print(b+a)