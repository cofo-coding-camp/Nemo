class Solution:
    def climbStairs(self, n: int) -> int:
        def cache(f):
            store = {}
            def cached(n):
                if n in store:
                    return store[n]
                else:
                    store[n] = f(n)
                    return store[n]
            return cached
        
        @cache
        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return dp(n - 1) + dp(n - 2)

        return dp(n)