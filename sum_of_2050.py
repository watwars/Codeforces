
def check_2050(n):
    rem = n % 2050
    if rem != 0:
        return -1
    ans = 0
    rem = n // 2050
    while rem > 0:
        ans += rem % 10
        rem = rem // 10
    return ans


def main():
    count = int(input())
    for i in range(count):
        num = int(input())
        print(check_2050(num))

main()
