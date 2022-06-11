name = input()
if len(name) > 100:
    raise Exception("Name can contain at most 100 letters")
    
distinctChar = {}

for char in name:
    rep = name.count(char)
    distinctChar[char] = rep

[print("CHAT WITH HER!") if len(distinctChar) % 2 == 0 else print("IGNORE HIM!")]