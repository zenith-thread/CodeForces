initialCost, money, bananaReq = list(map(int,input().split()))

borrow = 0
totalCost = 0

for i in range(1, bananaReq+1):
    totalCost += i * initialCost

borrow = totalCost - money
if borrow < 0:
    borrow = 0

print(borrow)