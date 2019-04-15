from random import choice
from random import randint
from collections import defaultdict

class EdgeSample:
    def __init__(self):
        self.edgeList = []
        self.hood = defaultdict(set)

    def add(self,u,v):
        self.edgeList.append((u, v))
        self.hood[u].add(v)
        self.hood[v].add(u)

    def remove(self):
        rand = randint(0, len(self.edgeList) - 1)
        uDel, vDel = self.edgeList.pop(rand)
        try:
            self.hood[uDel].remove(vDel)
            self.hood[vDel].remove(uDel)
        except: pass
        return uDel, vDel

    def getInter(self,u,v):
        return list(set(self.hood[u]) & set(self.hood[v]))


