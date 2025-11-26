import sys

def main():
    t = int(sys.stdin.readline().rstrip())

    for i in range(t):
        h, w, n = map(int, sys.stdin.readline().rstrip().split())
        if n % h != 0:
            floor = n % h
            room = n // h + 1
        else:
            floor = h
            room = n // h

        print(str(floor) + str("{:02d}".format(room)))

if __name__ == '__main__':
    main()