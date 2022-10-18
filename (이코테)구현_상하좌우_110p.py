# 조건 : 여행가 A는 N x N크기의 정사각형 공간 위에 서있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
#        가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
#        각 L R U D (좌 우 상 하)를 입력받으며 도착 지점을 찾는다.
#        (1, 1) 지점에서 L U 를 입력받으면 공간을 벗어나므로 무시된다.
# 입력 조건 : 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 ≤ N ≤ 100)
#            둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 ≤ 이동 횟수 ≤ 100)
# 출력 조건 : 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (x, y)를 공백으로 구분하여 출력한다.

# 1번 풀이
n = int(input())
plans = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_plan = ['L', 'R', 'U', 'D']


for plan in plans:
    for i in range(len(move_plan)):
        if plan == move_plan[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)

# 2번 풀이
n = int(input())
x, y = 1, 1
move_plans = ['L', 'R', 'U', 'D']
plans = input().split()
for plan in plans:
    if plan == 'L' and y < 0:
        y -= 1
    elif plan == 'R' and y < n:
        y += 1
    elif plan == 'U' and x < 0:
        x -= 1
    elif plan == 'D' and x < n:
        x += 1
print(x, y)
