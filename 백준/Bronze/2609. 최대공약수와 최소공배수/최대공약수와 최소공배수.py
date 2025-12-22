import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    # print(max(n, m))

    for i in range(1, max(n, m)+1):
        if n % i == 0 and m % i == 0:
            gcd = i
        lcm = n * m / gcd

    print("%d %d" % (gcd, lcm))

if __name__ == "__main__":
    main()