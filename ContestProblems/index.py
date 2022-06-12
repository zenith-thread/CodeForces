n = list(map(int, input().split()))

if not (1 <= len(n) <= 1000):
    raise Exception("Input must be in range: 1 <= n <= 1000")

index = []
for i in range(len(n)):
    if n[i] == 0:
        index.append(i + 1)

[print(i,end=" ") for i in index]