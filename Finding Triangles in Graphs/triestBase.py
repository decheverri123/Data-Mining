from Edges import Edges
from collections import defaultdict
import random


class TriestBase:
    def __init__(self,M):
        self.memory = M
        self.sample = Edges()
        self.globalT = 0
        self.localT = {}
        self.t = 0

    

    def flipCoin(self):
        return random.random() <= self.memory/self.t


    # can edge be inserted?
    def reservoirSample(self, u, v):
        if self.t <= self.memory: return True

        # no space, flip coin to remove random edge
        elif self.flipCoin():
            uDel, vDel = self.sample.removeEdge()
            self.updateCount(uDel,vDel,'-')
            return True
        
        return False

    def updateCount(self, u, v, op):
        
        commonNeighbors = self.sample.getIntersection(u,v)
        if not commonNeighbors: return

        for c in commonNeighbors:

            if op == '+':
                self.globalT += 1
                if c in self.localT: self.localT[c] += 1
                else: self.localT[c] = 1

                if u in self.localT: self.localT[u] += 1
                else: self.localT[u] =1

                if v in self.localT: self.localT[v] += 1
                else: self.localT[v] = 1

            elif op == '-':
                self.globalT -= 1
                self.localT[c] -= 1

                if self.localT[c] == 0: self.localT.pop(c)
                
                self.localT[u] -= 1
                
                if self.localT[u] == 0: self.localT.pop(u)
                
                self.localT[v] -= 1
                
                if self.localT[v] == 0: self.localT.pop(v)

    

    def returnCounters(self):
        
        estimate = max(1,
                    (self.t * (self.t - 1) * (self.t - 2)) / (self.memory * (self.memory - 1) * (self.memory - 2)))
        
        estimate -=1

        totalTriangles = int(estimate * self.globalT)

        for key in self.localT:
            self.localT[key] = int(self.localT[key] * estimate)

        return {'totalTriangles':totalTriangles,'localTriangles':self.localT}

    def run(self,u,v):
        self.t += 1
        if self.reservoirSample(u,v):
            self.sample.addEdge(u,v)
            self.updateCount(u,v,'+')
