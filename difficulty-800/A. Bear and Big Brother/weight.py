limak, bob = list(map(int, input().split())) 

if limak > bob or limak < 1 or bob > 10:
    raise Exception("Respective weights must be in order 1 <= Limak <= Bob <= 10")  

years = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    years += 1

print(years)