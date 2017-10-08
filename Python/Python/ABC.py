# https://open.kattis.com/problems/abc

def main():
    numbers = input().split()
    letters = list(input())
    numbers.sort(key=int)
    letterNumber = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2]}
    for letter in letters:
        print(letterNumber[letter], end = ' ')
main()
