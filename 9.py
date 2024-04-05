n, k, r = map(int, input().split())
counter = 0
while n <= r:
    n += (k / 100) * n
    counter += 1
print(counter + 1)