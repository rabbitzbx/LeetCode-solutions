# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # DFS
        if not node:
            return node
        self.dic = {}
        return self.createNode(node)
        
    def createNode(self, node):
        newNode = UndirectedGraphNode(node.label)
        self.dic[newNode.label] = newNode
        
        for neighbor in node.neighbors:
            if neighbor.label not in self.dic:
                self.createNode(neighbor)
            newNode.neighbors.append(self.dic[neighbor.label])
        
        return newNode
