import sys

def main():
    lst = [int(sys.stdin.readline().rstrip()) for i in range(10)]

    for i in range(len(lst)):
        lst[i] %= 42
    
    result = set(lst)
    print(len(result))


if  __name__ == "__main__":
    main()