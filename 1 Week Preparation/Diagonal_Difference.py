def DD(n):
    worklist = []
    for i in range(n):
        usr = map(int, input().split())
        worklist.append(list(usr))
    # worklist = [[1, 2, 3],
    #             [4, 5, 6],
    #             [9, 8, 9]]
    a = 0
    b = 0
    for j in range(n):
        a += worklist[j][j]
        b += worklist[j][-(1+j)]

    ans = a - b
    if ans < 0:
        print(-1*ans)

    else:
        print(ans)


if __name__=="__main__":
    n = int(input())
    # n = 3
    DD(n)