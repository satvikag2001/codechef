res=[]
for _ in range(int(input())):
    N= int(input())
    A=input()
    B=input()
    a=A.count('1')
    b=B.count('1')
    if a==b:
        res.append("YES")
    else:
        res.append("NO")
for r in res:
    print(r)