import numpy as np
import torch

from torch import nn


def log_softmax(x):
    """
        -1表示按照行相加

    :param x:
    :return:
    """
    return x - x.exp().sum(-1).log().unsqueeze(-1)


def nll(input, target):
    return -input[range(target.shape[0]), target].mean()


class CrossEntropy(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input, target):
        """
            log_softmax(input):

            log(exp(x)/sum(exp(x), dim=1) =
                x - log(sum(exp(x), dim=1))

            negative likelihood loss:

            ce = -ylog_softmax(input)

        :param input:
        :param target:
        :return:
        """
        # 1. 求解log_softmax
        print(input.exp().sum(dim=1).log())

        """
            input.exp().sum(dim=1)将(n, c)变成(n,)
            因此使用unsqueeze(1)变成(n, 1)
        """
        input = input - input.exp().sum(dim=1).unsqueeze(1).log()

        # 2. 求解negative likelihood loss
        ce = -input[range(len(target)), target].mean()

        return ce


if __name__ == "__main__":
    input = torch.tensor(
        np.array([[0.9826, 1.0630, -0.4096],
                  [-0.6213, 0.2511, 0.5659],
                  [0.5662, 0.7360, -0.6783],
                  [-0.4638, -1.4961, -1.0877],
                  [1.8186, -0.2998, 0.1128]]))

    target = torch.tensor([1, 0, 2, 1, 1])
    loss_fn = nn.CrossEntropyLoss()

    loss_fn1 = CrossEntropy()
    print(loss_fn1(input, target))

    print(loss_fn(input, target))
