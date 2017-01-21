if __name__ == "__main__":
    import itertools
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    import itertools

    l = [j for i in [range(0,x+1),range(0,y+1),range(0,z+1)] for j in i]
    r = list(map(list, list(filter(lambda x: sum(x) != 2, set(itertools.combinations(l,3))))))
    r.sort()
    print(r)
