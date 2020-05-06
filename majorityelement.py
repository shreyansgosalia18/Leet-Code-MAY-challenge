class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        snl = list(set(nums))
        for i in range(len(snl)):
            if nums.count(snl[i]) > len(nums)/2 : return snl[i]