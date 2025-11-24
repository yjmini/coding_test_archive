import sys

def main():
    lst = list(map(str, sys.stdin.readline().rstrip().split()))
    print(len(lst))




if __name__ == "__main__":
    main()