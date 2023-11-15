# 1번 : 스네이크 / 16435번 / 실버5

# 문제
# 스네이크버드는 뱀과 새의 모습을 닮은 귀여운 생물체입니다. 
# 스네이크버드의 주요 먹이는 과일이며 과일 하나를 먹으면 길이가 1만큼 늘어납니다.
# 과일들은 지상으로부터 일정 높이를 두고 떨어져 있으며 i (1 ≤ i ≤ N) 번째 과일의 높이는 hi입니다. 
# 스네이크버드는 자신의 길이보다 작거나 같은 높이에 있는 과일들을 먹을 수 있습니다.
# 스네이크버드의 처음 길이가 L일때 과일들을 먹어 늘릴 수 있는 최대 길이를 구하세요.

# 입력
# 첫 번째 줄에 과일의 개수 N (1 ≤ N ≤ 1,000) 과 스네이크버드의 초기 길이 정수 L (1 ≤ L ≤ 10,000) 이 주어집니다.
# 두 번째 줄에는 정수 h1, h2, ..., hN (1 ≤ hi ≤ 10,000) 이 주어집니다.

# 출력
# 첫 번째 줄에 스네이크버드의 최대 길이를 출력합니다.

import sys
input = sys.stdin.readline

N, L = map(int,input().split())
snList = list(map(int,input().split()))

snList.sort()

for i in snList:
    if(i <= L):
        L+=1
    else:
        break
print(L)

# 2번 : 국회의원 선거 / 1417번 / 실버5

# 문제
# 다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있다. 다솜이는 이 기계를 이용해서 2008년 4월 9일 국회의원 선거를 조작하려고 한다.
# 다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다.
# 현재 형택구에 나온 국회의원 후보는 N명이다. 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.
# 다솜이는 기호 1번이다. 다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다. 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선된다.
# 예를 들어서, 마음을 읽은 결과 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면, 다솜이는 2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하면, 국회의원에 당선이 된다.
# 돈으로 매수한 사람은 반드시 다솜이를 찍는다고 가정한다.
# 다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 후보의 수 N이 주어진다. 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄에 걸쳐 입력이 들어온다. N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())

fList = []
for i in range(N):
    fcount = int(input())
    fList.append(fcount)


dasom = fList[0]
sortList = fList[1:]
sortList.sort()
count = 0

if(N==1):
    print(0)
else:
    while dasom <= max(sortList):
        sortList[-1]-=1
        dasom+=1
        count+=1
        sortList.sort()
    print(count)

# 3번 : 폴리오미노 / 1343번 / 실버5

# 문제
# 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
# 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

# 출력
# 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.

import sys
input = sys.stdin.readline

N = str(input().rstrip())

N = N.replace("XXXX","AAAA")
N = N.replace("XX","BB")

if(N.__contains__("X")):
    print(-1)
else:
    print(N)