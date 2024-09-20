# Linear regression

## Gradient descent with proof

We have a linear equation $y = ax + b$ that we need to ajust to a set of training data $T$ so it minimises a loss function $\mathcal{L}$. For this, we'll choose $\mathcal L (y, \hat y) = {1 \over |T|} \sum_{y \in T}(y - \hat y)^2  where $\hat y$ is the expected output. Since the loss function is convex (ie. $\mathcal{L}''(x) = 0 \geq 0$), we can apply the conventional gradient descent algorithm without worrying about local minimas. But before, we'll have to figure out $\mathcal L (y, \hat y) \over da$ and $\mathcal  L (y, \hat y) \over db$ in order to figure out for each step of the training which way we need to move our parameters.

We have,
$$
\begin{aligned}
{ L (y, \hat y) }             &= {1 \over |T|} \sum_{y \in T} (a^2x^2 + 2axy + y^2 - 2 \hat yax - 2y \hat y + \hat y^2) \\

{ d L (y, \hat y) \over da }    &= {1 \over |T|} \sum_{y \in T} (2ax^2 + 2xy - 2 \hat y x) \\
                                &= {2 \over |T|} \sum_{y \in T} x(ax + y - \hat y) \\ 
                                &= {2 \over |T|} \sum_{y \in T} x(y - \hat y) \\

{ d L (y, \hat y) \over db }    &= {2 \over |T|} \sum_{y \in T} (y - \hat y)
\end{aligned}
$$

Thus,

$$
a_{n+1} = a_n + \alpha {2 \over |T| }\sum_{y \in T} x(y - \hat y) \\
b_{n+1} = b_n + \alpha {2 \over |T| }\sum_{y \in T} (y - \hat y)
$$