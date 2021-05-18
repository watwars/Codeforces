def find_step(n):
    steps = 0
    current = 5
    while n > 0:
        steps += n // current
        n = n % current
        current -= 1
    print(steps)


def main():
    count = int(input())
    find_step(count)



main()