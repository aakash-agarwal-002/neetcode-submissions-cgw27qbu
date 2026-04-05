class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}

        def dp(target):
            if target < 0:
                return float('inf')
            if target in memo.keys():
                return memo[target]
            if target == 0:
                return 0
                
            res = float('inf')
            for coin in coins:
                need = dp(target-coin)+1
                res = min(res,need)

            memo[target] = res
            return  memo[target]

        ans = dp(amount)
        return -1 if ans == float('inf') else ans