class   LinearRegression :
    n_a = float(0)
    n_b = float(0)
    a   = float(0)
    b   = float(0)
    t = 0
    learning_rate = float(0)
    l_loss    = []
    epoch   = 0

    def __init__(self, lr : float = 0.1) -> None:
        self.learning_rate = lr

    def normalized_infer(self, x):
        return self.n_a * x + self.n_b
    
    def infer(self, x):
        return self.a * x + self.b

    def loss(self,  x: list, y : list):
        return sum([(self.normalized_infer(x[i]) - y[i]) ** 2 for i in range(len(x))]) / len(x)

    def rmse(self,  x: list, y : list):
        return sum([(self.infer(x[i]) - y[i]) ** 2 for i in range(len(x))]) ** -2 / len(x)

    def step(self, x: list, y : list):
        m = len(x)
        da = 0
        db = 0
        F = self.learning_rate / m
        for i in range(m):
            d = self.normalized_infer(x[i]) - y[i]
            db += d * F
            da += d * x[i] * F
        self.n_a -= da
        self.n_b -= db

    def denorm_params(self):
        m       = ((self.ymax - self.ymin) / (self.xmax - self.xmin))
        self.a  = self.n_a * m
        self.b  = (self.n_b * (self.ymax - self.ymin) + self.ymin) - self.a * self.xmin

    def norm(self, x : list, lmin : float, lmax : float) -> list:
        return [(i - lmin) / (lmax - lmin) for i in x]

    def train(self, x: list, y : list):
        self.xmin = min(x)
        self.xmax = max(x)
        self.ymin = min(y)
        self.ymax = max(y)
        self.n_x = self.norm(x, self.xmin, self.xmax)
        self.n_y = self.norm(y, self.ymin, self.ymax)
        self.l_loss.append(self.loss(self.n_x, self.n_y))
        while True :
            pre_loss    = self.l_loss[self.epoch]
            self.step(self.n_x, self.n_y)
            post_loss   = self.loss(self.n_x, self.n_y)
            self.l_loss.append(post_loss)
            self.epoch += 1
            if pre_loss <= post_loss:
                self.denorm_params()
                print(f"Normalized parameters : a={self.n_a} b={self.n_b}")
                print(f"Denormalize parameters : a={self.a} b={self.b}")
                break
