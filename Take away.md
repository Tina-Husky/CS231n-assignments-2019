## Some take away ...

1. Iterating Over Arrays

   https://numpy.org/doc/1.17/reference/arrays.nditer.html#arrays-nditer

2. NumPy Broadcasting    (critical & interesting)

   http://cs231n.github.io/python-numpy-tutorial/

3. Softmax derivative

   https://math.stackexchange.com/questions/945871/derivative-of-softmax-loss-function

4.  Introduction of fundamental concepts of [PyTorch](https://github.com/pytorch/pytorch)

   https://github.com/jcjohnson/pytorch-examples#pytorch-custom-nn-modules

5. Backprop of Batch Normalization

   https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html  (straightforward & interesting)

   http://cthorey.github.io./backpropagation/  (breathtaking... & confusing)

6. [Unbiased Estimation](./ref/unbiased_estimator.pdf)

   https://www.math.arizona.edu/~jwatkins/N_unbiased.pdf

7. Backprop in Convolutional Layer

   https://medium.com/@2017csm1006/forward-and-backpropagation-in-convolutional-neural-network-4dfa96d7b37e

8. 



Questions the come up when doing assignments:

1. When calculating $\frac{\partial l}{\partial W}$ ( $dW$ for short) via Backprop, does $dW$ need to be divided by $N$ (i.e. train_num or batch_size) ? I observed $dW$ in `linear_SVM` in `assigment1` does, but the rest doesn't. Is there any rules that I can follow?

   ***Answer:*** It depends on forward formulations. If there is $\frac{1}{N}$ in one formulation, when the stream flows back to this, $dW$ need to be divided by $N$, vice versa.

2. 