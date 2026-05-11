class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        ltr = [  ]
        sum = 1
        for i in nums:
            item = sum * i
            sum = item
            ltr.append(item)
        rtl = [1] * len(nums)
        sum = 1
        for i in range(len(nums)-1, -1, -1):
            item = sum * nums[i]
            sum = item
            rtl[i]= item
        res = []
        for i in range(len(nums)):
            if i ==0:
                res.append( 1 * rtl[i+1])
            elif i == len(nums)-1:
                res.append(ltr[i-1])
            else:
                res.append(ltr[i-1] * rtl[i+1])

        return res
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        pre = [1] * n
        product = 1
        for i in range(n):
            pre[i] = product
            product *= nums[i]
        
        suff = [1] * n
        product = 1
        for i in range(n-1, -1, -1):
            suff[i] = product
            product *= nums[i]

        res = [1] * n
        for i in range(n):
            res[i] = pre[i] * suff[i]
        return res

        