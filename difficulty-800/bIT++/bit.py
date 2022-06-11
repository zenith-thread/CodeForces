x = 0
n = int(input())

if n < 1  or n > 150:
    raise ValueError("[INPUT ERROR]:\nInput must 1 <= n <= 150\n") 

commands = [input() for i in range(n)]

for command in commands:
    if "++" in command:
        x += 1
    else:
        x -= 1

print(x) 