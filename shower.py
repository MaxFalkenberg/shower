import numpy as np

class shower:

    def __init__(self,L):
        self.L = L
        self.tank = int(L/2)
        self.s = []
        self.tank_store = []

    def run_original(self,N):
        for i in range(N):
            if self.tank < self.L:
                self.tank += 1
            if np.random.rand() > 0.5:
                if self.tank > 1:
                    self.tank -= 2
                    self.s.append(2)
                elif self.tank == 1:
                    self.tank -= 1
                    self.s.append(1)
                else:
                    self.s.append(0)
            else:
                self.s.append(0)
            self.tank_store.append(self.tank)

    def run(self,N):
        for i in range(N):
            self.tank_store.append(self.tank)
            if self.tank == L:
                self.tank -= 1
                self.s.append(-1)
            elif self.tank == 0:
                self.tank += 1
                self.s.append(1)
            else:
                if np.random.rand() > 0.5:
                    self.tank -= 1
                    self.s.append(-1)
                else:
                    self.tank += 1
                    self.s.append(1)

    def null(self,N):
        for i in range(N):
            if self.tank < self.L:
                self.tank += 1
            if np.random.rand() > 0.5:
                self.s.append(2)
                self.tank -= 2
            else:
                self.s.append(0)
            self.tank_store.append(self.tank)

    def sum(self,M):
        cumsum = np.cumsum(self.s).astype('float')
        self.sigma = []
        for i in np.arange(1,M,10):
            self.sigma.append(np.var((cumsum[i:]-cumsum[:-i])))
