import numpy as np
#from pocketpla import PocketPLA

class LinearRegression:
    def fit(self, _X, _y):
        _X = np.array(_X)
        _y = np.array(_y)
        #_X = np.hstack((_X, np.ones((_X.shape[0], 1)))) caso n estivesse os 1 no timeRL
        arg1 = _X.T @ _X
        arg2 = _X.T @ _y
        inversa = np.linalg.pinv(arg1)
        self.w = inversa  @  arg2
     
    def predict(self, _x):
    # _x = np.hstack((_x, np.ones((_x.shape[0], 1))))
     return _x @ self.w

    def getW(self):
        return self.w

class LRClassifier():
    def fit(self, _X, _y):
        lr = LinearRegression()
        lr.fit(_X, _y)
        self.w = lr.getW()
        
        #pla = PocketPLA()
        #pla.set_w(self.w)
        #pla.execute(_X, _y)
        #self.w = pla.get_w()
        
        
    def predict(self, _X):
        return [np.sign(np.dot(self.w, x)) for x in _X]
     
    def getRegressionY(self, regressionX, shift=0):
        return (-self.w[0]+shift - self.w[1]*regressionX) / self.w[2]