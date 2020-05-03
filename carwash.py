import json
import random

with open("data.json", "r+") as file:
    data = json.load(file)


def main():

    print('\n Welcome \n')
    while True:
        people_choice = input('if you want to wash your car input yes(y) if no input no ')
        if people_choice == "y":
            district = choose_district()
            car = choose_car()
            code = gift_code()
            check_choice(district,car,code)
            get_data(district,car,code)
            break
        elif people_choice == 'no':
            print('\n Always ready to help you when you need it \n')
            break
        else:
            print('Incorrect input')


def choose_district():
    while True:
        district_choice = input('\n We have four car-washing companies choose the best for you:' + data['district'][0] + ", "+ data['district'][1] + ", " + data['district'][2] + ", " + data['district'][3])
        district_choice = district_choice.upper()
        if district_choice in data['district']:
            return district_choice
        else:
            print('\nIncorrect input')

def choose_car():
    while True:
        type = input('\n Which of the following types is your car:' + data['car_type'][0] + ", " + data['car_type'][1])
        type = type.upper()
        if type in data['car_type']:
            return type
        else:
            print('\n Incorrect input')

def gift_code():
    code = []
    your_letters = 'abcdefghifvwqzxp1234567890'
    for i in range(1, 5):
        x = random.choice(your_letters)
        code.append(x)
    code = "".join(code)
    return code

def check_choice(car_wash_choice, car_type, code):

        if car_wash_choice == 'ZEYTUN':
            print('\n Our adress is Zeytun Rubinynac 14 working from 9:00 - 19:00 \n')

            if car_type == 'JEEP':
                print('5000  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)


            elif car_type == 'SEDAN':
                print('2500  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)



        elif car_wash_choice == 'KOMITAS':
            print('\n Our adress is Komitas Griboedov 20 working 24 hours \n')

            if car_type == 'JEEP':
                print('6000  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)

            elif car_type == 'SEDAN':
                print('3500  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)



        elif car_wash_choice == 'NOR-NORK':
            print('\n Our adress is Nor-Nork Mikoyan 13 working from 9:00 - 23:00 \n')

            if car_type == 'JEEP':
                print('4000  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)

            elif car_type == 'SEDAN':
                print('2000  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)



        elif car_wash_choice == 'EREBUNI':
            print('\n Our adress is Erebuni Avanesov 14 working from 9:00 - 22:00 \n')

            if car_type == 'JEEP':
                print('2500  amd  / if you want to reserve you can call +374-98-29-88-27.Use the code to get a free drink while waiting',code)

            elif car_type == 'SEDAN':
                print('1500  amd  / if you want to reserve you can call +374-98-29-88-27. Use the code to get a free drink while waiting',code)

def get_data(choose_district, car_type, code):
    with open("data.json", "r+") as file:
        data = json.load(file)

    file_name = 'car.json'
    json_data = {'district': choose_district,
                 'car': car_type,
                 'code': code
    }
    my_data = []
    my_data.append(json_data)

    with open(file_name, 'a') as f:
        json.dump(my_data, f, indent=2)


main()
