teams = list(input())

count = 1
for i in range(len(teams)):
    try:
        if teams[i] == teams[i+1]:
            count += 1
            if count == 7:
                break
        else:
            count = 1
    except IndexError:
        pass

print("YES") if count >= 7 else print("NO") 