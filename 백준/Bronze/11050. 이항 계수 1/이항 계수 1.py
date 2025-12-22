import sys

def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    result = int(factorial(n)/(factorial(k)*factorial(n-k)))

    print(result)

def factorial(num):
    if num ==0 or num==1:
        return 1
    
    return num*factorial(num-1)

if __name__ == "__main__":
    main()