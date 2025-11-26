import sys

def main():
    string = sys.stdin.readline().rstrip()

    alphabet = [-1] * 26

    for i in range(len(string)):
        if alphabet[ord(string[i]) - 97] == -1:
            alphabet[ord(string[i]) - 97] = i

    for i in range(len(alphabet)):
        print(alphabet[i], end=" ")

if __name__ == "__main__":
    main()