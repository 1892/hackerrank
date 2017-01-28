if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    l = []
    for i in range(0, n):
        l.append(list(map(int, input().split())))
        
    k = int(input())

    l.sort(key=lambda i:i[k])

    for j in l:
        print(*j)