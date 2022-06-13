s = []
nl = []
kl = []

t = int(input())
if not (1 <= t <= 10000):
    raise Exception("number of test examples must be within range (1 <= t <= 10000)")

for i in range(t):
    n, k = list(map(int, input().split())) 
    if not (1 <= k <= n <= 200000):
        raise Exception("Input must be within range: 1 <= k <= n <= 200000")
    nl.append(n)
    kl.append(k)
    s.append(input())

count = []
for i in range(t):
    c = 0
    for j in range(kl[i]):
        if s[i][j] == "W":
            c += 1
    count.append(c)

# print(count)
[print(i) for i in count]