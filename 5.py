n = int(input())
for x in range(1, n ** 2):
    if x ** 3 <= n:
        print(x ** 3)
