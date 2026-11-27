
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        INF = -10**9

        dp = [INF] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            factor, price = items[i]

            # Count free items obtained from buying this item
            free = sum(
                items[j][0] % factor == 0
                for j in range(n) if j != i
            )

            buy = [INF] * (budget + 1)

            for cost in range(price, budget + 1):
                # First purchase gives free items
                first = dp[cost - price] + free + 1

                # Additional purchases give only one item
                again = buy[cost - price] + 1

                buy[cost] = max(first, again)

            # Choose whether to buy this item type
            dp = [
                max(dp[c], buy[c])
                for c in range(budget + 1)
            ]

        return max(dp)
