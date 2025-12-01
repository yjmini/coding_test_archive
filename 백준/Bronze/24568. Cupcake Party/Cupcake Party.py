import sys

def main():
    big = int(sys.stdin.readline().rstrip())
    small = int(sys.stdin.readline().rstrip())

    print(big * 8 + small * 3 - 28)

if __name__ == "__main__":
    main()