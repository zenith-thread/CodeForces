n = int(input())        # number of problems in contest
if n < 1  or n > 100:
    raise ValueError("[INPUT ERROR]:\nInput must 1 <= n <= 100\n") 

solve = 0
words = [list(map(int,input().split())) for i in range(n)]       # surity of each member for each problem

for word in words:
    if word.count(1) > 1:
        solve += 1
print(solve)