#Buradaki sorular leetcode dan alinmistir.

#Integer formunda verilmis iki array den bulmamiz istenen bir target var. Target'i saglayan iki elemani cikti olarak vermemiz gerekli.
#Ornek olarak Input:nums = [2,7,11,15], target = 9
#Output:[0,1]
#Aciklama : nums[0] + nums[1] == 9 oluyor. Bu yuzden [0,1] return ediyoruz.

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            i+=1

#Kodlari bize istedigimiz ciktiyi verecektir.
