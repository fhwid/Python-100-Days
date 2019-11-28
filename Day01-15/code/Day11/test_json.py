import json


def main():
    mydict = {
        'name': '罗浩',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白远方'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 300}
        ]
    }
    try:
        with open('data.json', 'w', encoding= 'utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('game over!')



if __name__ == "__main__":
    main()


