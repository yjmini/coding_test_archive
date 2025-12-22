import sys

def main():
    while True:
        n = sys.stdin.readline().rstrip()
        if n == "0":
            break

        is_palindrome = True

        for i in range(len(n)//2):
            if n[i] != n[-(i+1)]:
                is_palindrome = False
                break

        if is_palindrome:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()