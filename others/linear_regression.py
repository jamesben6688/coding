from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


class LinearRegression:
    def __init__(self, lr=1e-3, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # X: (n, h)
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias

            dw = 1 / n_samples * np.dot(X.T, y_pred - y)
            db = 1 / n_samples * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred


def mse(y_test, y_pred):
    return np.mean((y_test-y_pred) ** 2)


if __name__ == '__main__':
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    plt.scatter(X[:, 0], y, color='b', marker='o', s=30)
    # plt.show()

    reg = LinearRegression(lr=0.01)
    reg.fit(X_train, y_train)
    predictions = reg.predict(X_test)

    print(mse(y_test, predictions))

    y_pred_line = reg.predict(X)
    plt.plot(X, y_pred_line, color='black')
    plt.show()
