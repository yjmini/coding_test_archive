import sys

def main():
    T = int(sys.stdin.readline().rstrip())

    for i in range(T):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())

        people = [j for j in range(1, n+1)]

        for f in range(k):
            for l in range(1, n):
                people[l] += people[l-1]
            
        print(people[-1])


if __name__ == "__main__":
    main()