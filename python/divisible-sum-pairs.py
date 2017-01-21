if __name__ == "__main__":
    n, m = list(map(int, input().split(" ")))

    arr = list(map(int, input().split(" ")))

    k = 0

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) % m == 0:
                k += 1    
    print(k)