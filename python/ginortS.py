if __name__ == "__main__":
    key_s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
    d = {i : key_s.index(i) for i in key_s}
    s = input().strip("\r")
    print(*sorted(s, key=lambda x:d.get(x)), sep="")
