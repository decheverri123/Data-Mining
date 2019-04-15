import random
from EdgeSample import EdgeSample
from collections import defaultdict

class TriestBase:


    
    def __init__(self,M):
        self.M = M
        self.edgeSample = EdgeSample()
        self.localTri = defaultdict()
        self.totalTri = 0
        self.t = 0


    def flipCoin(self):
        return random.random() <= self.M/self.t

    def sampEdge(self,u,v):
        if self.t <= self.M: return True

        elif self.flipCoin():
            uDel, vDel = self.edgeSample.remove()
            self.updateCount(uDel,vDel,'-')
            return True
        
        return False

    def updateCount(self, u, v, op):
        
        comm = self.edgeSample.getInter(u,v)
        
        if not comm: return


        if op == '+':
            self.totalTri += 1

            if v in self.localTri:
                self.localTri[v] += 1

            for shared in comm:
                if shared in self.localTri:
                    self.localTri[shared] += 1
                self.localTri[shared] = 1

        elif op == '-':
            
            self.totalTri -= 1

            if u in self.localTri:
                self.localTri[u] -= 1
                if self.localTri[u] == 0: self.localTri.pop(u)
            
            if v in self.localTri:
                self.localTri[v] -= 1
                if self.localTri[v] == 0: self.localTri.pop(v)

            for shared in comm:
                if shared in self.localTri:
                    self.localTri[shared] -= 1
                    if self.localTri[shared] == 0: self.localTri.pop(shared)

    

    def getCount(self):
        varFormula = (self.t * (self.t - 1) * (self.t - 2))/(self.M * (self.M - 1) * (self.M - 2))
        estimate = max(1, varFormula)
        totalEst = int(estimate) * self.totalTri
        totalEst = abs(totalEst)

        for key in self.localTri:
            self.localTri[key] = int(self.localTri[key] * estimate)
        

        return {'total':totalEst,'local':self.localTri}

    def run(self,u,v):
        self.t += 1
        if self.sampEdge(u,v):
            self.edgeSample.add(u,v)
            self.updateCount(u,v,'+')
