## target : 14
## nums = [4,1,9,7,5,3,16]

def twoSum(nums, target):
    nums.sort()
    l,r = 0,len(nums)-1
    while l<r:
        if nums[l]+nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
        return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))