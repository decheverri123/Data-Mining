from random import choice
from random import randint
from collections import defaultdict

class EdgeSample:
    def __init__(self):
        self.edgeList = []
        self.hood = defaultdict(set)

    def add(self,u,v):
        self.edgeList.append((u,v))
        self.editHood('+',u,v)

    def remove(self):
        rand = randint(0,len(self.edgeList)-1)
        uDel,vDel = self.edgeList.pop(rand)
        
        

        self.editHood('-',uDel,vDel)
        return uDel, vDel

    def getInter(self,u,v):
        try: return self.hood[u].intersection(self.hood[v])
        except: return None


    def editHood(self,op,u,v):
        if op == '+':
            self.hood[u].add(v)
            self.hood[v].add(u)

        elif op == '-':
            try:
                self.hood[u].remove(v)
                self.hood[v].remove(u)
            except:
                pass

            if not self.hood[u]: self.hood.pop(u)

            if not self.hood[v]: self.hood.pop(v)
