
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE1 = 100019
        BASE2 = 100043

        def check(length):
            power1 = pow(BASE1, length, MOD1)
            power2 = pow(BASE2, length, MOD2)

            h1 = h2 = 0

            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2

            freq = {(h1, h2): 1}

            for i in range(length, n):
                old = nums[i - length]
                new = nums[i]

                h1 = (h1 * BASE1 + new - old * power1) % MOD1
                h2 = (h2 * BASE2 + new - old * power2) % MOD2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
