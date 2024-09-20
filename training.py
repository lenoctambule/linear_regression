from model import LinearRegression
import matplotlib.pyplot as plt
import csv

if __name__ == "__main__" :
    model = LinearRegression()
    training = {'x' : list(), 'y' : list()}
    with open('data.csv', 'r') as f :
        reader = csv.DictReader(f, delimiter=',')
        for l in reader:
                training['x'].append(float(l['km']))
                training['y'].append(float(l['price']))
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
    plt.plot(model.l_loss)
    plt.show()

