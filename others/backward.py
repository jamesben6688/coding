from einops import *
import numpy as np
import matplotlib.pyplot as plt


class Softmax:
    def __init__(self, train=True):
        self.grad = None
        self.train = train

    def forward(self, x, y):
        prob = np.exp(x-np.max(x, axis=1, keepdims=True))
        prob /= np.sum(prob, axis=1, keepdims=True)

        if self.train:
            loss = -np.sum(np.log(prob[range(len(y)), y]))/len(y)

            self.grad = prob.copy()
            self.grad[range(len(y)), y] -= 1
            self.grad /= len(y)
            return prob, loss

        else:
            return prob

    def backward(self):
        return self.grad


class Linear:
    def __init__(self, in_channels, out_channels, lr):
        self.w = np.random.rand(in_channels, out_channels)
        self.b = np.random.rand(out_channels)
        self.lr = lr

    def forward(self, x):
        self.x = x
        output = einsum(x, self.w, 'b c1, c1 c2 -> b c2') + self.b
        return output

    def backward(self, prev_grad):
        cur_grad = einsum(rearrange(self.x, 'b c -> c b'), prev_grad, 'c1 b, b c2 -> c1 c2')

        self.w -= self.lr * cur_grad
        self.b -= self.lr * np.sum(prev_grad, axis=0)
        return cur_grad


class Network:
    def __init__(self, in_channels, out_channels, n_classes, lr):
        self.lr = lr
        self.linear = Linear(in_channels, out_channels, lr)
        self.softmax = Softmax()

    def forward(self, x, y=None):
        out = self.linear.forward(x)
        out = self.softmax.forward(out, y)
        return out

    def backward(self):
        grad = self.softmax.backward()
        grad = self.linear.backward(grad)

        return grad


if __name__ == "__main__":
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

    # x = np.concatenate([np.array([[1]] * data.shape[0]), data[:, :2]], axis=1)
    x = data[:, :-1]
    y = data[:, -1:].flatten()

    net = Network(2, 2, 2, 0.1)
    # loss_fn = CrossEntropy(n_classes=2)
    for epoch in range(500):
        prob, loss = net.forward(x, y)
        # loss = loss_fn.forward(out, y)
        # grad_ = loss_fn.backward()
        grad = net.backward()
        print(loss)

    for d in data:
        if d[2] == 0:
            plt.scatter(*d[:2], color='red')
        else:
            plt.scatter(*d[:2], color='green')


    net.softmax.train = False
    test_data = np.array([[0, 0], [0, 4], [8, 6], [10, 10]])
    res = net.forward(np.array([[0, 0], [0, 4], [8, 6], [10, 10]]))
    res = np.argmax(res, axis=1)
    for i in range(len(test_data)):
        if res[i] == 0:
            plt.scatter(*test_data[i], color="blue")
        else:
            plt.scatter(*test_data[i], color='pink')
    plt.show()
    # print(net.forward(np.array([[0, 0], [0, 4], [8, 6], [10, 10]])), y)


