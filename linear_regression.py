
class   LinearRegression :
    a = float(0)
    b = float(0)
    t = 0
    lr = float(0)
    L = list()

    def __init__(self, lr : float = 0.1) -> None:
        self.lr = lr

    def inferY(self, x):
        return self.a * x + self.b

    def train(self, x : float, y : float, m)-> None :
        da  = (self.lr / m) * (self.inferY(x) - y) * x
        db  = (self.lr / m) * (self.inferY(x) - y)
        self.a -= da
        self.b -= db

    def train_batch(self, x: list, y : list):
        m = len(x) if len(x) > len(y) else len(y)
        for i in range(m):
            self.train(x[i], y[i], m)