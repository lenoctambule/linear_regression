class   LinearRegression :
    a = float(0)
    b = float(0)
    t = 0
    learning_rate = float(0)
    L = list()

    def __init__(self, lr : float = 0.1) -> None:
        self.learning_rate = lr

    def infer(self, x):
        return self.a * x + self.b

    def loss(self,  x: list, y : list):
        return sum([(self.infer(x[i]) - y[i]) ** 2 for i in range(len(x))]) / len(x)

    def rmse(self,  x: list, y : list):
        return sum([(self.infer(x[i]) - y[i]) ** 2 for i in range(len(x))]) ** -2 / len(x)

    def step(self, x: list, y : list):
        m = len(x)
        da = 0
        db = 0
        F = self.learning_rate / m
        for i in range(m):
            d = self.infer(x[i]) - y[i]
            db += d * F
            da += d * x[i] * F
        self.a -= da
        self.b -= db
        print("b ", self.b, db)
        print("a ", self.a, da)
        return da, db

    def norm(self, x : list, lmin : float, lmax : float) -> list:
        return [(i - lmin) / (lmax - lmin) for i in x]

    def train(self, x: list, y : list):
        self.xmin = min(x)
        self.xmax = max(x)
        self.ymin = min(y)
        self.ymax = max(y)
        self.n_x = self.norm(x, self.xmin, self.xmax)
        self.n_y = self.norm(y, self.ymin, self.ymax)
        while True :
            #print(self.a, self.b)
            pre_loss    = self.loss(self.n_x, self.n_y)
            da, db      = self.step(self.n_x, self.n_y)
            #print(da, db)
            post_loss   = self.loss(self.n_x, self.n_y)
            if pre_loss <= post_loss:
                print(f"Parameters : a={self.a} b={self.b}")
                break
