# Linear regression

## Usage

```text
>$ py -m install requirements.txt
>$ py training.py
>$ py predict.py
Input mileage :230000      
Result : 3931.7570368074385
```

## Gradient descent

We have a linear equation $y = ax + b$ that we need to ajust to a set of training data $T$ so it minimises a loss function $L$. For this, we'll choose $L (y, \hat y) = {1 \over |T|} \sum_{y \in T}(y - \hat y)^2$ where $\hat y$ is the expected output. Since the loss function is convex (ie. $L''(x) \geq 0$), we can apply the conventional gradient descent algorithm without worrying about local minimas. But before, we'll have to figure out $L (y, \hat y) \over da$ and $\mathcal  L (y, \hat y) \over db$ in order to figure out for each step of the training which way we need to move our parameters.

We have,

$$\begin{aligned}
{L (y, \hat y)}             &= {1 \over |T|} \sum_{y \in T} (a^2x^2 + 2axy + y^2 - 2 \hat yax - 2y \hat y + \hat y^2) \\
{dL (y, \hat y) \over da }    &= {1 \over |T|} \sum_{y \in T} (2ax^2 + 2xy - 2 \hat y x) \\
                                &= {2 \over |T|} \sum_{y \in T} x(ax + y - \hat y) \\ 
                                &= {2 \over |T|} \sum_{y \in T} x(y - \hat y) \\
{ d L (y, \hat y) \over db }    &= {2 \over |T|} \sum_{y \in T} (y - \hat y)
\end{aligned}$$

Thus,

$$\begin{aligned} a_{n+1} &= a_n + {\alpha \over |T| }\sum_{y \in T} x(y - \hat y)\\  
b_{n+1} &= b_n + {\alpha \over |T| }\sum_{y \in T} (y - \hat y)
\end{aligned}$$


Where $\alpha$ is the learning rate.
