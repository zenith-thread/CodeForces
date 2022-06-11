n, t = list(map(int,input().split()))

if not (n >= 1) and not (t <= 50):
    raise Exception("input must be in 1 >= n, t <= 50")

queue = list(input())

if len(queue) > n:
    raise Exception("queue must be of size n")

for j in range(t):
    s = []
    for i in range(n):
        if queue[i] == "B":
            s.append(i)  
    try:
        for i in s:
            queue[i], queue[i+1] = queue[i+1], queue[i] 
    except IndexError:
        pass

[print(student, end="") for student in queue]