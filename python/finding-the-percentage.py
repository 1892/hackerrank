if __name__ == '__main__':
    def av(l):
        return sum(l)/len(l)
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("{:.2f}".format(av(student_marks.get(query_name))))
