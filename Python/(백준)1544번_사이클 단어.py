# 문제
# 사이클 단어는 어떤 단어를 원형 모양으로 차례대로 쓴 것이다. 따라서, 어떤 단어를 이렇게 쓴 후에 임의의 단어를 고른다. 그 후에 시계방향으로 차례대로 읽으면 그 것이 단어가 된다. 만약에 단어 A와 단어 B가 있을 때, 단어 B를 원형으로 써서, 단어 A와 같이 읽을 수 있으면, 두 단어는 같은 단어이다. 따라서, picture와 turepic은 같은 단어다.

# N개의 단어가 주어졌을 때, 서로 다른 단어가 총 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 단어가 한 줄에 하나씩 주어진다. 단어는 영어 소문자로만 이루어져 있다. N은 50보다 작거나 같은 자연수이며, 단어의 길이는 최대 50이다.

# 출력
# 첫째 줄에 서로 다른 단어가 몇 개인지 출력한다.

import sys
input = sys.stdin.readline
N = int(input())

wordList=[]
for i in range(N):
    word = input().rstrip()
    wordList.append(word)
print("wordList",wordList)

result = []

for word in wordList:
    for i in range(len(word)):
        result.append(word[i:] + word[:i])

count = 0
result = set(result)
print(result)
for word in wordList:
    if(word not in result):
        count+=1
print(count)
    
        

   
    
