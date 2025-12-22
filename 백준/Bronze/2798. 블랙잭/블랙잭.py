import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cards = list(map(int, sys.stdin.readline().rstrip().split()))
    result = 0

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                sum = cards[i] + cards[j] + cards[k]
                if sum <= m and sum > result:
                    result = sum

    print(result)

if __name__ == "__main__":
    main()