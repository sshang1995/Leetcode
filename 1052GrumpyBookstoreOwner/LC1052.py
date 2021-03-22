class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # get already satisfied customer.
        cus = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:# he is happy
                cus += customers[i]
                customers[i] =0
  
        # get optimal number, sliding window, x is window size.
        curr_cus = max_cus =0
        for i, num in enumerate(customers):
            curr_cus += num # add current to rolling total
            if i >= X:# remove some previou one
                curr_cus -= customers[i-X]
            max_cus = max(max_cus, curr_cus)
        return cus + max_cus
            