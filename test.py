from linear_regression import LinearRegression
import random as rand
import math
import matplotlib.pyplot as plt

m = LinearRegression(lr = 0.000001)
training = [list(), list()]
test     = [list(), list()]
with open('data.csv', 'r') as f :
    lines = f.readlines()
    l     = len(lines) - 1
    tmp   = [i for i in range(l)]
    rand.shuffle(tmp)
    for i in range(1, l) :
        s = lines[i].split(',')
        if True: 
            training[0].append(float(s[0]))
            training[1].append(float(s[1]))
        if True :
            test[0].append(float(s[0]))
            test[1].append(float(s[1]))
m.train_batch(training[0], training[1])
error = 0
for i in range(len(test[0])):
    res = m.inferY(test[0][i])
    error += (res - test[1][i]) ** 2
plt.scatter(test[0], test[1])
#plt.show()
rmse = math.sqrt(error) / len(test[0])
print(f'{rmse=}')
