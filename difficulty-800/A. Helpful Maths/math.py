prob = input().split("+")
prob.sort()
for i in range(len(prob)-1):
    print(f"{prob[i]}+",end="")
print(prob[-1])