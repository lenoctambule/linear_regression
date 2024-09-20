import json

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
    while 1 :
        try:
            mileage = float(input('Input mileage :'))
            break
        except ValueError:
            print('ERROR : Input a valid float.')
            exit(1)
    print(f'Result : {a * mileage + b}')