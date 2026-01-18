t = int(input())

for i in range(t):
    lst = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    for j in range(9):
        if (len(set(lst[j])) != 9):
            result = 0
            break
        vertical_list = []

        for k in range(9):
            vertical_list.append(lst[k][j])
        # print(vertical_list)
        if (len(set(vertical_list)) != 9):
            result = 0
            break

        for l in range(0, 9, 3):
            for m in range(0, 9, 3):
                square = []
                for n in range(3):
                    for o in range(3):
                        square.append(lst[l+n][m+o])
                if (len(set(square)) != 9):
                    result = 0
                    break

    print("#{} {}".format(i+1, result))