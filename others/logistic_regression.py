"""
    逻辑回归是分类问题
    y = w0 + w1*x1 + w2*x2

    = [1, x1, x2] * [w0,
                     w1,
                     w2]

    X = [1 x1 x2]
    W = [w0, w1, w2]

    y = x*w^T
    z = sigmod(y) = 1 / (1+exp(-XW^T))

    dz/dw = X^T(1/(1+exp(-XW))-Y) = X^T(h-y)

    求导公式推导: https://laobadao.github.io/2017/10/27/logistic-cost/index.html
    
    

    决策边界:
        w0+w1x1+w2x2 = 0

        x2 = - (wo+w1x1) / w2
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[2, 1, 0],
                 [2, 2, 0],
                 [5, 4, 1],
                 [4, 5, 1],
                 [2, 3, 0],
                 [3, 2, 0],
                 [6, 5, 1],
                 [4, 1, 0],
                 [6, 3, 1],
                 [7, 4, 1]])


class Classifier:
    def __init__(self, epoches, lr):
        self.epoches = epoches
        self.lr = lr

    def draw(self, x, y):
        plt.scatter(x[:, 1][y.reshape(-1, ) == 0],
                    x[:, 2][y.reshape(-1, ) == 0],
                    color="red", marker="^", s=150)

        plt.scatter(x[:, 1][y.reshape(-1, ) == 1],
                    x[:, 2][y.reshape(-1, ) == 1],
                    color="green", s=150)

        w0, w1, w2 = self.w
        x1 = np.linspace(0, 10, 10)
        x2 = - (w0 + w1 * x1) / w2

        plt.plot(x1, x2)
        plt.show()

    def train(self, x, y):
        self.w = np.random.rand(x.shape[1], 1)
        self.draw(x, y)
        for i in range(self.epoches):
            h = 1 / (1 + np.exp(-np.dot(x, self.w)))

            print(i, np.sum(-y*np.log(h)))

            dw = np.dot(x.T, h - y)
            self.w -= self.lr * dw

        self.draw(x, y)

    def predict(self, x):
        x = np.concatenate([np.array([[1]] * x.shape[0]), x], axis=1)
        h = 1 / (1 + np.exp(-np.dot(x, self.w)))
        return 1 if h >= 0.5 else 0


x = np.concatenate([np.array([[1]] * data.shape[0]), data[:, :2]], axis=1)
y = data[:, -1:]

cls = Classifier(1000, 0.01)
cls.train(x, y)
# print(cls.w)
print(1 / (1 + np.exp(-np.dot(x, cls.w))))
# print(cls.predict(np.array([[0, -2]])))

