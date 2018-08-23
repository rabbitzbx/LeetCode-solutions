class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Kahn's algorithm
        result = []
        graph = [[] for i in range(numCourses)]
        degrees = [0 for i in range(numCourses)]

        for cur, pre in prerequisites:
            graph[cur].append(pre)
            degrees[pre] += 1

        stack = []
        for i in range(numCourses):
            # node with no incoming edge
            if degrees[i] == 0:
                stack.append(i)
        while stack:
            i = stack.pop()
            numCourses -= 1
            result.insert(0, i)
            for j in graph[i]:
                degrees[j] -= 1
                if degrees[j] == 0:
                    stack.append(j)

        if not numCourses:
            return result

        return []
