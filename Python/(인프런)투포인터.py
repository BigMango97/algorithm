# Two sum
# 정수가 저장된 배열 nums이 주어졌을 때, nums 원소중 두 숫자를 더해서 target이 될 수 있으면 True
# 불가능하면 False를 반환하세요. 같은 원소를 두번 사용할 수 없습니다.

# input : nums ={4,1,9,7,5,3,16} target : 14
# output : True

# input : nums = {2,1,5,7} target : 4
# output : False

def twosum(nums, target):
    nums.sort()
    left = 0
    right = len(nums)-1
    while left<right:
        if(nums[left]+nums[right]<target):
            left +=1
        elif(nums[left]+nums[right]>target):
            right -=1
        elif(nums[left]+nums[right]==target):
            return True
    return False


print(twosum(nums=[4,1,9,7,5,3,16], target=14))
print(twosum(nums=[2,1,5,7], target=4))