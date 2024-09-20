import json

if __name__ == "__main__" :
    try:
        mileage = float(input('Input mileage :'))
    except ValueError:
        print('Usage : py predict.py <mileage:float>')
        exit(1)
    a = 0
    b = 0
    try :
        with open('params.json', 'r') as f:
            d = json.loads(f.read())
            a = d['a']
            b = d['b']
    except :
        pass
    print(f'Result : {a * mileage + b}')