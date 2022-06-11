from curses.ascii import isupper
word = input()

if not (0 < len(word) <= 100):
    raise Exception("String length must be between 1 and 100") 

upper = 0
lower = 0
for letter in word:
    if isupper(letter):
        upper += 1
    else:    
        lower += 1
if upper > lower:
    word = word.upper()
else:
    word = word.lower()

if __name__ == "__main__":
    print(word)