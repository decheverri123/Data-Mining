from Edges import Edges
from collections import defaultdict
from random import random

class TriestImpr:
    def __init__(self,M):
        self.memory = M
        self.sample = Edges()
        self.globalT = 0
        self.localT = {}
        self.t = 0

    def reservoirSample(self, u, v):
        
        return self.t <= self.memory and self.flipCoin

    def updateCount(self, u, v, op):
        
        common_neighborhood = self.sample.getIntersection(u,v)
        
        if not common_neighborhood: return

        incTri = max(1,
                    int(((self.t - 1) * (self.t - 2)) / (self.memory * (self.memory - 1))))
        
        incTri -= 1

        for c in common_neighborhood:

            if op == '+':

                self.globalT += incTri
                
                if c in self.localT: self.localT[c] += incTri
                else: self.localT[c] = incTri

                if u in self.localT: self.localT[u] += incTri
                else: self.localT[u] = incTri

                if v in self.localT: self.localT[v] += incTri
                else: self.localT[v] = incTri


    def flipCoin(self):
        return random() <= self.memory/self.t

    def returnCounters(self):
        return {'totalTriangles':self.globalT,'localTriangles':self.localT}

    def run(self,u,v):
        self.t += 1
        self.updateCount(u,v,'+')
        if self.reservoirSample(u,v): self.sample.addEdge(u,v)
