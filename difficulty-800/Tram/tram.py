n = int(input())    #  number of stops

route = [list(map(int, input().split())) for i in range(n)]
if route[0][0] != 0 or route[n-1][1] != 0:
    raise ValueError("First and Last value must be zero")

entered = 0
exited = 0
inTram = 0
maxinTram = 0

for i in range(n):
    exited += route[i][0]
    entered += route[i][1]    
    inTram = entered - exited
    if maxinTram < inTram:
        maxinTram = inTram
    if inTram < 0:
        raise Exception("Number of people exited the tram can't be greater than number of people in tram")

if inTram - route[n-1][0] > 0:
    raise Exception("Everyone must board off the tram at the last stop")

print(maxinTram)