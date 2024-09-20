from model import LinearRegression
import random as rand
import math
import matplotlib.pyplot as plt
import numpy as np

m = LinearRegression()
training = {'x' : list(), 'y' : list()}
with open('data.csv', 'r') as f :
    lines = f.readlines()
    l     = len(lines) - 1
    tmp   = [i for i in range(l)]
    rand.shuffle(tmp)
    for i in range(1, l) :
        s = lines[i].split(',')
        if True: 
            training['x'].append(float(s[0]))
            training['y'].append(float(s[1]))
m.train(training['x'], training['y'])
print('RMSE =', m.rmse(training['x'], training['y']))
xmin = min(training['x'])
xmax = max(training['x'])
ymin = m.infer(xmin)
ymax = m.infer(xmax)
plt.plot([xmin, xmax], [ymin, ymax])
plt.scatter(training['x'], training['y'])
#plt.plot([0, 1], [ymin, ymax])
#plt.scatter(m.n_x, m.n_y)
plt.show()
