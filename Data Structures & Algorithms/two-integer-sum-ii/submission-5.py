class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex = 0;
        rightIndex = len(numbers) - 1

        while leftIndex < rightIndex:
            total = numbers[leftIndex] + numbers[rightIndex]
            if total == target:
                return [leftIndex + 1, rightIndex + 1]
            elif total < target:
                leftIndex += 1
            else: 
                rightIndex += -1 