s, t = [input().lower() for i in range(2)]

# if not (0 < len(s) <= len(t) <= 100):
    # raise Exception("Input must be in 0 < s <= t <= 100")
# 
reverse = s[::-1]
[print("YES") if t == reverse else print("NO")]