import sys

def main():
    while True:
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        if a == 0 and b == 0 and c == 0:
            break
        elif a*a + b*b == c*c:
            print("right")
        elif a*a + c*c == b*b:
            print("right")
        elif b*b + c*c == a*a:
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    main()