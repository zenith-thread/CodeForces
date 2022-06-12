m = int(input())

if not(1 <= m <= 2000):
    raise Exception("Length of string must be within range: (1 <= n <= 2000)")

n = input()

if len(n) != m:
    raise Exception("Length of string must be equal n provided")

string = [i for i in n]
start = 0
end = len(string) - 1
index = []

for i in range(len(string)//2 + 1):
    try:
        index.append((string[-1],end))
        index.append((string[-2],start))
        start += 1
        end -= 1
        [string.pop() for i in range(2)]
    except IndexError:
        pass 

index.sort(key=lambda i:i[1])
[print(index[i][0],end="") for i in range(len(n))]