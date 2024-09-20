from model import LinearRegression
import random as rand
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    model = LinearRegression()
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

    model.train(training['x'], training['y'])
    model.export_params()
    print('RMSE =', model.rmse(training['x'], training['y']))
    xmin = min(training['x'])
    xmax = max(training['x'])
    ymin = model.infer(xmin)
    ymax = model.infer(xmax)
    plt.subplot(1,2,1)
    plt.plot([xmin, xmax], [ymin, ymax], color="red")
    plt.scatter(training['x'], training['y'], color="black", marker="x")
    plt.subplot(1,2,2)
    plt.plot([i for i in range(model.epoch+1)], model.l_loss)
    plt.show()

