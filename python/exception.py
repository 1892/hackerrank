n = int(input())

l = []
for i in range(0,n):
    l.append(input().split(" "))
    
for i in l:
    try:
        print(int(i[0]) / int(i[1]))
    except Exception as e:
        print ("Error Code:",e)