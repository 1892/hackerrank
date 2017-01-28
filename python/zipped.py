if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    l = []
    for i in range(0, m):
        l.append(list(map(int, input().split())))
        
    ll = zip(*l)

    for j in ll:
        print(sum(j)/len(j))