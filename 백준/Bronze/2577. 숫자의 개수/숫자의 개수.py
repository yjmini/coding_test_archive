import sys


def main():
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    c = int(sys.stdin.readline().rstrip())
    mul = a * b * c

    # print(mul)
    lst = [0]*10 

    while (mul > 0):
        temp = mul % 10
        mul = mul // 10
        lst[temp] += 1
    
    #print(lst)

    for i in range(len(lst)):
        print(lst[i])

if __name__ == "__main__":
    main()