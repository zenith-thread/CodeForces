n = int(input())
if n < 1 or n > 50:
    raise Exception("stones must be 1 <= n <= 50") 

stone = input()
if len(stone) != n:
    raise Exception("String of color must be same as number of stones") 

neighbour = 0

for i in range(len(stone)):
    try:
        if stone[i] == stone[i+1]:
            neighbour += 1
    except IndexError:
        pass

print(neighbour)