from random import random
from EdgeSample import EdgeSample
from collections import defaultdict

class TriestImpr:
    def __init__(self,M):
        self.M = M
        self.edgeSample = EdgeSample()
        self.totalTri = 0
        self.localTri = defaultdict(set)
        self.t = 0

    def sampled(self,u,v):
        if self.t <= self.M: return True

        elif self.flipCoin():
            uDel, vDel = self.edgeSample.remove()
            self.edgeSample.editHood('-',uDel,vDel)
            return True
        return False

    def updateCount(self, u, v, op):
        
        common = self.edgeSample.getInter(u,v)
        
        if not common: return
        varFomula = ((self.t - 1) * (self.t - 2)) // (self.M * (self.M - 1))
        
        inc = max(1, varFomula)

        for neighbor in common:

            if op == '+':
                self.totalTri += inc
                
                try: self.localTri[neighbor] += inc
                except TypeError: self.localTri[neighbor] = inc
                
                try: self.localTri[u] += inc
                except TypeError: self.localTri[u] = inc
                
                try: self.localTri[v] += inc
                except TypeError: self.localTri[v] = inc
            
            if op == '-':
                self.totalTri -= inc
                
                try: self.localTri[neighbor] -= inc
                except TypeError: self.localTri[neighbor] = inc
                
                try: self.localTri[u] -= inc
                except TypeError: self.localTri[u] = inc
                
                try: self.localTri[v] -= inc
                except TypeError: self.localTri[v] = inc



    def flipCoin(self):
        return random() <= self.M/self.t

    def getCount(self):
        return {'total':self.totalTri,'local':self.localTri}

    def run(self,u,v):
        self.t += 1
        self.updateCount(u,v,'+')
        if self.sampled(u,v):
            self.edgeSample.add(u,v)
