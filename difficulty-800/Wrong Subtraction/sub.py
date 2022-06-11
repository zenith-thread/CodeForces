n, k = list(map(int, input().split()))

if not (2 <= n <= 1000000000) or not (1 <= k <= 50):
    raise Exception("n and k must be in the range: 2 <= n <= 1000000000, 1 <= k <= 50)")

for i in range(k):
    if n % 10 == 0:
        n = n//10
    else:
        n = n-1

print(n)