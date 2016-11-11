
import bisect
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sum_list, cur_sum, count = [],0,0
        for num in nums:
            cur_sum+=num  #get the sum of all numbers before current number
            if lower <=cur_sum<=upper:
                count +=1
            if not sum_list:
                sum_list.append(cur_sum)
                continue
            low = cur_sum -lower # sum[j]-sum[i] <upper -> sum[j]-upper < sum[i]
            hi = cur_sum - upper # sum[j]-sum[i] >lower -> sum[j]-lower > sum[i]
            idx_lo = bisect.bisect_right(sum_list,low)
            idx_hi = bisect.bisect_left(sum_list,hi)
            count +=abs(idx_lo-idx_hi)
            bisect.insort(sum_list,cur_sum) #insert current sum and sort the sum list
        return count
