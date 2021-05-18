def print_word(word):
    length = len(word)
    if length <= 10:
        print(word)
        return
    answer = word[0] + str(length - 2) + word[length - 1]
    print(answer)


def main():
    count = int(input())
    for i in range(count):
        word = input()
        print_word(word)



main()