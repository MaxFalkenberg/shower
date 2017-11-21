import numpy as np
import pickle
import os
import binascii

class shower:

    def __init__(self,L,p=0.5,load = False):
        self.L = L
        self.tank = int(L/2)
        self.s = []
        self.N = 0
        self.tank_store = []
        self.p = p
        self.var_M = []
        self.M = []
        if load != False:
            with open (load + '/meta.pickle', 'rb') as fp:
                self.L,self.N,self.p = pickle.load(fp).values()
            self.tank_store = np.load(load + '/tank_store.npy')
            self.s = np.load(load + '/s.npy')
            self.var_M = list(np.load(load + '/var_M.npy'))
            self.M = np.load(load + '/M.npy')
            if len(self.tank_store) != 0:
                self.tank = self.tank_store[-1]
            else:
                self.tank = int(L/2)

    def run_original(self,N):
        for i in range(N):
            if self.tank < self.L:
                self.tank += 1
            if np.random.rand() > p:
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
            self.N += 1
            self.tank_store.append(self.tank)
            if self.tank == self.L:
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

    def sum(self,M,step = 10):
        cumsum = np.cumsum(self.s).astype('float')
        self.sigma = []
        for i in np.arange(1,M,step):
            self.sigma.append(np.var((cumsum[i:]-cumsum[:-i])))

    def log_sum(self,M,n):
        cumsum = np.cumsum(self.s).astype('float')
        self.var_M = []
        self.M = np.logspace(0,M,n,dtype = 'int')
        for i in self.M:
            self.var_M.append(np.var((cumsum[i:]-cumsum[:-i])/i))

    def save(self,foldername=None):
        files = {'L':self.L,'N':self.N,'p':self.p}
        if foldername == None:
            folder = str('shower_L' + str(self.L) + '_N' + str(self.N) +
                                        '_p' + str(self.p) + '_' +
                                        binascii.b2a_hex(os.urandom(6)))
        else:
            folder = foldername
        os.makedirs(folder)
        with open(folder + '/meta.pickle', 'wb') as f:
            pickle.dump(files, f)
        np.save(folder + '/tank_store',self.tank_store)
        np.save(folder + '/s',self.s)
        np.save(folder + '/var_M',self.var_M)
        np.save(folder + '/M',self.M)
