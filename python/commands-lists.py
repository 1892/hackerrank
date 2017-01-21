if __name__ == "__main__":
    N = int(input())
    commands = []
    l = []
    for i in range(0,N):
        commands.append(input().split(" "))
    for command in commands:
        if command[0] == "insert":
            l.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            l.remove(int(command[1]))
        elif command[0] == "append":
            l.append(int(command[1]))
        elif command[0] == "sort":
            l.sort()
        elif command[0] == "reverse":
            l.reverse()
        elif command[0] == "pop":
            l.pop()
        elif command[0] == "print":
            print(l)