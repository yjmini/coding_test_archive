import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    size = list(map(int, sys.stdin.readline().rstrip().split()))
    t, p = map(int, sys.stdin.readline().rstrip().split())

    t_bundle = 0

    for i in range(len(size)):
        if size[i] % t == 0:
            t_bundle += size[i] // t
        else:
            t_bundle += size[i] // t + 1
    
    print(t_bundle)
    print("{} {}".format(n // p, n % p))

if __name__ == "__main__":
    main()