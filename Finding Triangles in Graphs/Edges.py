from collections import defaultdict
import random

class Edges:
    def __init__(self):

        self.edgeList = set()
        self.neighborHood = defaultdict(set)
        self.edgeCount = 0

    def addEdge(self, u, v):
        self.edgeList.add((u, v))
        self.neighborHood[u].add(v)
        self.neighborHood[v].add(u)

    def removeEdge(self):
        
        uDel, vDel = self.edgeList.pop()  #set pops are inherently random

        if not self.neighborHood[uDel]: self.neighborHood.pop(uDel)

        if not self.neighborHood[vDel]: self.neighborHood.pop(vDel)
        
        return uDel, vDel


    def getIntersection(self, u, v):
        
        if u in self.neighborHood and v in self.neighborHood:
            return self.neighborHood[u].intersection(self.neighborHood[v])

        return None


