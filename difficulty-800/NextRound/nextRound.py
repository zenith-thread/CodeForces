from exceptions import Exception

e = Exception()

n , k = list(map(int,input().split())) 
e.checkInput(n, k)

scores = list(map(int,input().split()))
e.checkScore(scores)
e.checkScoreOrder(scores)
kPlaceScore = 0
try:
    kPlaceScore = scores[k - 1]
except IndexError:
    pass

count = 0

for i in range(n):
    if scores[i] >= kPlaceScore and scores[i] != 0:
        count += 1

if __name__ == "__main__":
    print(count)