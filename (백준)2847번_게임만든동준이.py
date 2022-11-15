# 2847번 게임만든동준이
# 문제) 학교에서 그래픽스 수업을 들은 동준이는 수업시간에 들은 내용을 바탕으로 스마트폰 게임을 만들었다. 게임에는 총 N개의 레벨이 있고, 각 레벨을 클리어할 때 마다 점수가 주어진다. 플레이어의 점수는 레벨을 클리어하면서 얻은 점수의 합으로, 이 점수를 바탕으로 온라인 순위를 매긴다. 동준이는 레벨을 난이도 순으로 배치했다. 하지만, 실수로 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우를 만들었다.
#       이 문제를 해결하기 위해 동준이는 특정 레벨의 점수를 감소시키려고 한다. 이렇게해서 각 레벨을 클리어할 때 주는 점수가 증가하게 만들려고 한다.
#       각 레벨을 클리어할 때 얻는 점수가 주어졌을 때, 몇 번 감소시키면 되는지 구하는 프로그램을 작성하시오. 점수는 항상 양수이어야 하고, 1만큼 감소시키는 것이 1번이다. 항상 답이 존재하는 경우만 주어진다. 정답이 여러 가지인 경우에는 점수를 내리는 것을 최소한으로 하는 방법을 찾아야 한다.
# 입력) 첫째 줄에 레벨의 수 N이 주어진다. (1 ≤ N ≤ 100) 다음 N개 줄에는 각 레벨을 클리어하면 얻는 점수가 첫 번째 레벨부터 마지막 레벨까지 순서대로 주어진다. 점수는 20,000보다 작은 양의 정수이다.
# 출력) 첫째 줄에 점수를 몇 번 감소시키면 되는지 출력한다.

N = int(input())
# 추후 쉽게 계산하기 위해서 기존 리스트를 뒤집기
a_list = []
for i in range(N):
    a = int(input())
    a_list.append(a)
a_list_reverse = a_list[::-1]
# i, i+1를 비교해가며 숫자 정렬,,
i_list = []
for i in range(0, N-1):
    if a_list_reverse[i] <= a_list_reverse[i+1]:
        while a_list_reverse[i] <= a_list_reverse[i+1]:
            a_list_reverse[i+1] -= 1
        i_list.append(a_list_reverse[i])
    elif a_list_reverse[i] > a_list_reverse[i+1]:
        i_list.append(a_list_reverse[i])
# 마지막에 나온 숫자에서 -1하기
i_list.append(i_list[-1]-1)
i_list_reverse = i_list[::-1]

total = 0
for i in range(0, len(i_list_reverse)):
    between = a_list[i]-i_list_reverse[i]
    total += between
print(total)
