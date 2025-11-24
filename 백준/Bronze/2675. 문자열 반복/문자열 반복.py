import sys

input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    iterator, str = input().rstrip().split()
    for j in range(len(str)):
        print(str[j] * int(iterator), end="")
    print()