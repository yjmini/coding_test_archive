import sys

def main():
    num = int(sys.stdin.readline().rstrip())
    scores = list(map(int, sys.stdin.readline().rstrip().split()))

    max_score = max(scores)

    for i in range(num):
        scores[i] = scores[i] / max_score * 100

    result = sum(scores) / num
    print(result)
    
if __name__ == "__main__":
    main()