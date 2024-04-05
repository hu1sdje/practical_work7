n = int(input())
s = 1
counter = 0
for i in range(1, n // 2):
    if s < n:
        s *= 2
        print(s // 2)
    else:
        break