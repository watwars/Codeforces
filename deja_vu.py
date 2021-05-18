
def add_char(string):
    for i in range(len(string) + 1):
        if string[len(string) - i - 1] != 'a':
            new_str = string[:i] + 'a' + string[i:]
            print("YES")
            print(new_str)
            return
    print("NO")


def main():
    count = int(input())
    for i in range(count):
        string = input()
        add_char(string)


main()