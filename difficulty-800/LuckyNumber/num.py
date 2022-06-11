num = input()

if not (1 <= int(num) <= 10**18):
    raise Exception("Number can only be in range 1 <= n <= 10^18")

lucky = 0
lucky += num.count('4') + num.count('7')

[print("YES") if lucky == 4 or lucky == 7 else print("NO")]