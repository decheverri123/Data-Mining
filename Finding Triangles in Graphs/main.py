from TriestBase import TriestBase
from TriestImpr import TriestImpr
import sys



results = []

iterations = 20

algoType = str(sys.argv[1])
sampleSize = int(sys.argv[2])
inputFile = str(sys.argv[3])


for i in range(iterations):

    if algoType == 'b':
        model = TriestBase(sampleSize)

    if algoType == 'i':
        model = TriestImpr(sampleSize)


    with open(inputFile) as f:
        for line in f:
            if line.startswith('%'): continue
            u, v = line.split()
            u, v = int(u), int(v)
            model.run(u, v)
            
        results.append(model.getCount()['total'])


print("Output vals",results)
