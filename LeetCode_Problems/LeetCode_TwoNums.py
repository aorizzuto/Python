"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
import itertools

def twoSum(nums, target):

    done = False

    sublist=[]

    for L in range(1,len(nums)):
        for subset in itertools.combinations(nums, L+1):
            sublist = list(subset)
            print(sublist)
            if sum(sublist) == target:
                done = True
                break
        if done:
            break
    
    if sublist != []:
        ret = []
        for i in range(len(sublist)):
            index = nums.index(sublist[i])
            ret.append(index)
            nums[index]="x"

        return ret
    return None



def main():
    # nums = [2,5,5,11]
    # target = 10
    # print(twoSum(nums, target))

    # nums = [0,4,3,0]
    # target = 0
    # print(twoSum(nums, target))

    nums = [-3,4,3,90]
    target = 0
    print(twoSum(nums, target))


if __name__ == '__main__':
    main()