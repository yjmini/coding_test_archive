import sys

def main():
    num = int(sys.stdin.readline().rstrip())
    result = 0
    
    for i in range(1, num+1):
        digit_sum = sum(map(int, str(i)))
        all_sum = i + digit_sum

        if all_sum == num:
            result = i
            break

    print(result)


if __name__ == "__main__":
    main()
