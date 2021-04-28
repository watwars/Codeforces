
def verify_vector(arr):
    x = 0
    y = 0
    z = 0
    for v in arr:
        x += int(v[0])
        y += int(v[1])
        z += int(v[2])
    if x == 0 and y == 0 and z == 0:
        print("YES")
    else:
        print("NO")


def main():
    count = int(input())
    nums = []
    for i in range(count):
        vector = input().split(" ")
        nums.append(vector)
    verify_vector(nums)


main()