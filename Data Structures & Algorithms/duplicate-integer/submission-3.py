class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = 0
        seenNumbers = []

        for num in nums:
            if (num in seenNumbers):
                return True
            seenNumbers.append(num)
        
        return False