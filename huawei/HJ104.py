


while True:
    try:
        n = int(input())
        l = []
        for i in range(n):
            s = input()
            l.append(s)
        for j in l:
            while (len(j) > 8):
                print(j[:8])
                j = j[8:]
            print(j.ljust(8, "0"))
    except:
        pass