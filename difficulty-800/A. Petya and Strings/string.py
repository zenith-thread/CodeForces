def checkString(string):
    for i in range(len(string[1])):
        if string[0][i] != string[1][i]:
            if ord(string[0][i]) < ord(string[1][i]):
                return -1
            else:
                return 1
    return 0

if __name__ == "__main__":
    string = [input().lower() for i in range(2)]

    if len(string[0]) == len(string[1]):
        s = checkString(string)
        print(s)
    else:
        raise Exception("Both Strings must be of same lengths!")