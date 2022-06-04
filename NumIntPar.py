from threading import Thread, Lock
import time
import math
import sys

class Shared_data:

    global_sum = 0
    mutex = Lock()

class worker(Thread):

    def __init__(self, myid, numThreads, numSteps, step, data):
        super(worker, self).__init__()
        self.data = data
        self.myid = myid
        self.numThreads = numThreads
        self.numSteps = numSteps
        self.step = step
        self.sum = 0.0

    def run(self):
        blocks = int(self.numSteps / self.numThreads)
        start = self.myid * blocks
        stop = start + blocks
        if self.myid == self.numThreads : stop = self.numSteps

        for i in range(start, stop):
            x = (i + 0.5) * self.step
            self.sum += 4.0 / (1.0 + x * x)

        self.data.mutex.acquire()
        self.data.global_sum += self.sum
        self.data.mutex.release()

class calcPiInThreads():

    # def __init__(numSTeps,numThreads):

    def calcPi(self,numSteps,numThreads):

        data = Shared_data()
        step = 1.0 / numSteps
        threads = []
        startTime = time.time()

        for i in range(numThreads):
            threads.append(worker(i, numThreads, numSteps, step, data))

        for i in range(numThreads):
            threads[i].start()

        for i in range(numThreads):
            threads[i].join()

        pi = data.global_sum * step

        endTime = time.time()
        # print(f'parallel program results with {numSteps} steps')
        # print(f'computed pi = {pi}')
        # print(f'difference between estimated pi and Math.PI = {abs(pi - math.pi)}')
        # print(f'time to compute = {(endTime - startTime) / 1000} seconds')

        return pi





#Test code
if __name__ == '__main__':

    numSteps = 0
    numThreads = 0

    if len(sys.argv) != 3:
        print('arguments:  number_of_steps number_of_threads')
        exit(1)
    try:
        numSteps = int(sys.argv[1])
        numThreads = int(sys.argv[2])
    except Exception as e:
        print(e)
        exit(1)

    object=calcPiInThreads()
    print(numSteps,numThreads)
    pi=object.calcPi(numSteps,numThreads)
    print(pi)