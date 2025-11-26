import sys

def main():
    t = int(sys.stdin.readline().rstrip())

    lst = [sys.stdin.readline().rstrip() for i in range(t)]
    
    score = [0] * t

    for i in range(len(lst)):
        streak = 1
        for j in str(lst[i]):
            if j == 'O':
                score[i] += 1 * streak
                streak += 1
            elif j == 'X':
                streak = 1

    for i in range(len(score)):
        print(score[i])

if __name__ == "__main__":
    main()