def compare_2list():
    # n = 0
    l1 = [1, 1, 6, 8]
    l2 = [6, 8]
    for i in range(len(l1)):
        if l1[i] in l2:
            n = l2.index(l1[i])
        else:
            return False
    # for i in range(n,len(l1)):
    #     if l1[i] != l2[j]:



if __name__ == '__main__':
    l1 = [1, 1, 6, 8]
    l2 = [8, 6]
    print(set(l2).issubset(l1))








