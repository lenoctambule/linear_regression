import json
import csv

if __name__ == "__main__" :
    a = 0
    b = 0
    try :
        with open('params.json', 'r') as f:
            d = json.loads(f.read())
            a = d['a']
            b = d['b']
    except :
        pass
    print(f'Parameters :\n{a=}\n{b=}')
    l_x = list()
    l_y = list()
    try :
        with open('data.csv', 'r') as f :
            reader = csv.DictReader(f, delimiter=',')
            for l in reader:
                l_x.append(float(l['km']))
                l_y.append(float(l['price']))
    except :
        print('Failed to read data.csv file.')
        exit(1)
    RMSE    = 0
    MAE     = 0
    MSE     = 0
    for i in range(len(l_x)) :
        y = a * l_x[i] + b
        RMSE    += (y - l_y[i]) ** 2
        MAE     += abs(y - l_y[i])
    MSE     = (RMSE) / len(l_x)
    RMSE    = (RMSE / len(l_x)) ** (1/2)
    MAE     = MAE / len(l_x)
    print(f'{RMSE = }\n{MSE = }\n{MAE = }')