
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    
    myDict = dict()
    for index,number in enumerate(nums):
        if number in myDict:
            return[myDict[number],index]
        
        else:
            myDict[target-number] = index
            

print( "\nInput: nums = [2,7,11,15], target = 9 \nOutput: "+ str(twoSum(nums=[2,7,11,15],target=9)))
print( "\nInput: nums = [3,2,4], target = 6 \nOutput: "+ str(twoSum(nums=[3,2,4],target=6)))
print( "\nInput: nums = [3,3], target = 6 \nOutput: "+ str(twoSum(nums=[3,3],target=6)) + "\n")

        