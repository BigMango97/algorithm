# N = int(input())
# NList = list(map(int,input().split()))
# NList.sort()
# print(NList[(N-1)//2])
total = []
C, R = map(int,input().split())
for i in range(C):
    CList = list(map(int,input().split()))
    total.append(CList)

sorted(total, key = lambda x: (x[1], x[2], x[3]), reverse=True)
print(total)