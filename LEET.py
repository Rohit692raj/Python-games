class Solution:
    def permute(self, nums):

        def helper(temp,mapp):
            if len(temp) == len(nums):
                return res.append(temp[:])

            for i in range(len(nums)):
                if not mapp[i]:
                    temp.append(nums[i])
                    mapp[i] = 1
                    helper(temp,mapp)
                    x = temp.pop()

                    mapp[x] -= 1
        temp = []
        map = [0] * len(nums)
        helper(temp,map)
        print(map)
        res=[]

        return res
a = [1,1,2]
ans = Solution()
print(ans.permute(a))