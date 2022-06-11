n = int(input())

if n < 1 or n > 1000000:
    raise Exception("input must be 1 <= n <= 1,000,000")

def distance(x):
    if x % 5 == 0:
        return x // 5
    return x // 5 + 1

if __name__ == "__main__":
    print(distance(n))