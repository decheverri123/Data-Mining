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

    
    def flipCoin(self):
        return random() <= self.M/self.t

    def sampled(self, u, v):

        uDel, vDel = None, None 
        
        if self.t <= self.M: return True

        elif self.flipCoin():
            uDel, vDel = self.edgeSample.remove()

        return uDel and vDel

    def updateCount(self, u, v):
        
        common = self.edgeSample.getInter(u,v)
        
        if not common: return
        varFomula = ((self.t - 1) * (self.t - 2)) // (self.M * (self.M - 1))
        
        inc = max(1, varFomula)

        for neighbor in common:

            try:
                self.localTri[neighbor] += inc
                self.totalTri += inc
                self.localTri[u] += inc
                self.localTri[v] += inc
            except:
                self.localTri[neighbor] = inc
                self.totalTri = inc
                self.localTri[u] = inc
                self.localTri[v] = inc
    

    def getCount(self):
        return {'total':self.totalTri,'local':self.localTri}

    def run(self,u,v):
        self.t += 1
        self.updateCount(u,v)
        if self.sampled(u,v):
            self.edgeSample.add(u,v)
