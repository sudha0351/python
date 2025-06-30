t = int(input())

for _ in range(t):
    query = input().split()
    kind, n = query[0], int(query[1])
   
    if kind == "odd":
        for i in range(n):
            print(2 * i + 1)
    elif kind == "even":
        for i in range(n):
            print(2 * i)# python
