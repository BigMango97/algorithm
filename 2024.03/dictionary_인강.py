# 키값은 중복 x
score = {
    'math':97,
    'eng':49,
    'kor':89
}
print(score['math'])
print('music' in score)

# in 시간 복잡도 빅오원을 가진다!
if('music' in score):
    print(score['music'])
else:
    score['music'] = 0
print(score)



def two_sum(nums, target):
    dict_nums={}
    for i in nums:
        dict_nums[i] = True

    for i in nums:
        target_value = target - i
        if target_value in dict_nums:
            return True
    return False
print(two_sum(map(int,input().split()),int(input())))


