from triestBase import TriestBase
from triestImpr import TriestImpr
from collections import abc





mode = 1
sampleSize = [5000, 10000, 20000, 30000, 40000]
iterations = 1
outputs = []
outputLocal = []
file = "in.txt"


def run():

    for sample in sampleSize:
        for it in range(iterations):
            if mode == 1: model = TriestBase(sample)
            else: model = TriestImpr(sample)

            with open(file) as f:
                for line in f:
                    if line.startswith('%'): continue

                    u, v = list(map(int, line.strip().split()))

                    model.run(u, v)

                # print("============ FINAL OUTPUT IS ====================")
                # print(model.returnCounters())

                # outputs.append(model.returnCounters()['totalTriangles'])
                # outputLocal.append(model.returnCounters()['localTriangles'])
                print("Sample Size:", sample, "Iteration:", it+1, "Triangle Count:", model.returnCounters()['totalTriangles'])



if __name__ == "__main__":
    run()    
