if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    print(students)
    min_el = min(students, key=lambda x:x[1])[1]
    #students.remove(min(students, key=lambda x:x[1]))
    for i in students:
        if i[1] == min_el:
            students.remove(i)
    r = [i[0] for i in students if i[1] == min(students, key=lambda x:x[1])[1]]
    for i in r:
        print(i)