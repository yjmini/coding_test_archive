import sys

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True

def main():
    n = int(sys.stdin.readline().rstrip())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0

    for i in lst:
        if is_prime(i) == True:
            count += 1


    print(count)
if __name__ == "__main__":
    main()