class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # 反向遍历列表，计算每个 room 所需 hp 的最小值，记为 hp[i][j]
        # hp[i][j] = max(1, min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j])
        # hp[len(dungeon) - 1][len(dungeon[0]) - 1] = max(1, 1 - dungeon[len(dungeon) - 1][len(dungeon[0]) - 1])

        if not len(dungeon) or not len(dungeon[0]):
            return 1
        m = len(dungeon)
        n = len(dungeon[0])
        hp = [[0 for j in range(n)] for i in range(m)]
        hp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 2, -1, -1):
            hp[i][n - 1] = max(1, hp[i + 1][n -1] - dungeon[i][n - 1])
        for j in range(n - 2, -1, -1):
            hp[m - 1][j] = max(1, hp[m - 1][j + 1] - dungeon[m - 1][j])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                hp[i][j] = max(1, min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j])
        return hp[0][0]
