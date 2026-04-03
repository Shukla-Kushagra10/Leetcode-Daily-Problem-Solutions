'''You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.
The grid contains a value coins[i][j] in each cell:
If coins[i][j] >= 0, the robot gains that many coins.
If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.
Note: The robot's total coins can be negative. Return the maximum profit the robot can gain on the route.'''
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')
        dp = [[[NEG_INF]*3 for _ in range(n)] for _ in range(m)]
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                if k > 0: 
                    dp[0][0][k] = 0
                dp[0][0][k] = max(dp[0][0][k], coins[0][0])
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0: 
                        continue
                    val = coins[i][j]
                    best = NEG_INF
                    for (pi, pj) in [(i-1, j), (i, j-1)]:
                        if pi >= 0 and pj >= 0:
                            if val >= 0:
                                best = max(best, dp[pi][pj][k] + val)
                            else:
                                if k > 0:
                                    best = max(best, dp[pi][pj][k-1])
                                best = max(best, dp[pi][pj][k] + val)
                    dp[i][j][k] = best
        return max(dp[m-1][n-1])