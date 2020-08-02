from collections import Counter
while True:
    try:
        s = input()
        count = Counter(s)
        ll = sorted(count.items(),key=lambda kv:(kv[1], kv[0]))
        print(ll)
    except:
        break