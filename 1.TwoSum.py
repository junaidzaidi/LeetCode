
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    #Initializing dictionary in order to keep track of required numbers to complete a pair
    myDict = dict()
    for index,number in enumerate(nums):
        #Checking if number exist in the dictionary then return the index of the pair
        if number in myDict:
            return[myDict[number],index]
        else:
            #Store (target-number) in the dictionary as a key so that we can directly check the other number in the dictionary which completes the pair.
            myDict[target-number] = index
            

print( "\nInput: nums = [2,7,11,15], target = 9 \nOutput: "+ str(twoSum(nums=[2,7,11,15],target=9)))
print( "\nInput: nums = [3,2,4], target = 6 \nOutput: "+ str(twoSum(nums=[3,2,4],target=6)))
print( "\nInput: nums = [3,3], target = 6 \nOutput: "+ str(twoSum(nums=[3,3],target=6)) + "\n")

        