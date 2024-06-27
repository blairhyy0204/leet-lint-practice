"""
Leetcode 797. All Paths From Source to Target
Link: https://leetcode.com/problems/all-paths-from-source-to-target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DAG: no need for visited list 
        # DFS
        self.result = []
        onGraph = []
        self.traverse(graph, 0, onGraph)
        return self.result

    def traverse(self, graph, s, onPath):
        onPath.append(s)
        
        # base
        if s == len(graph) - 1:
            self.result.append(onPath[:]) # need to copy onPath
            
        for i in graph[s]:
            self.traverse(graph, i, onPath)

        onPath.pop(-1)
        return

