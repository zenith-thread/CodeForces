from shutil import ExecError
from pyparsing import ExceptionWordUnicode


n = int(input())

if not ( 1 <= n <= 100000):
    raise Exception("n must be between range: 1 <= n <= 100000")

strength = list(map(int,input().split()))

if len(strength) != n:
    raise Exception("input doesn't match the n provided")

maxS = max(strength)
minS = min(strength)

numOfMaxS = 0
numOfMinS = 0

for i in range(len(strength)):
    if strength[i] == maxS:
        numOfMaxS += 1
    elif strength[i] == minS:
        numOfMinS += 1

[print(0) if maxS == minS else print(len(strength) - numOfMaxS - numOfMinS)]