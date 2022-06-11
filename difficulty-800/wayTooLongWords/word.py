n = int(input())        # number of words
if n < 1  or n > 100:
    raise ValueError("[INPUT ERROR]:\nInput must 1 <= n <= 100\n") 

words = [input().lower() for i in range(n)]
output = [word[0] + str(len(word)-2) + word[-1] if len(word) > 10 else word for word in words]
[print(abbr) for abbr in output]