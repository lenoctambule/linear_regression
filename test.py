from model import LinearRegression
import random as rand
import matplotlib.pyplot as plt

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
plt.subplot(1,2,1)
plt.plot([xmin, xmax], [ymin, ymax])
plt.scatter(training['x'], training['y'])
plt.subplot(1,2,2)
plt.plot([i for i in range(m.epoch+1)], m.l_loss)
plt.show()
