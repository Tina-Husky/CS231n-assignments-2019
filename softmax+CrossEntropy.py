import numpy as np
def softmax(X):
    eps = np.exp(X)
    return eps / np.sum(eps)

def stable_softmax(X):
    # avoid overflowing and resulting in nan
    eps = np.exp(X-np.max(X))
    return eps / np.sum(eps)

def cross_entropy(X, y):
    """
    X is the output from network. shape: (num_example, num_classes)
    y is label. shape: (num_example,)
        Note that y is not one-hot encoded vector
        It can be computed as y.argmax(axis=1) from one-hot encoded vectors of labels if required
    """
    m = y.shape[0]
    p = softmax(X)
    log_likelihood = -np.log(p[range(m)], y)
    loss = np.sum(log_likelihood) / m
    return loss
