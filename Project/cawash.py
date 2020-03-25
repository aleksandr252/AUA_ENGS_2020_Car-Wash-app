import json
print('\n Welcome \n')
people_choice = input('if you want to wash your car input yes(y) or no ') == 'y'
with open("data.json", "r+") as file:
    data = json.load(file)
while True:
    if people_choice:
        car_type = input(
            '\n Which of the following types is your car:' + data['car_type'][0] + ", " + data['car_type'][1])
        car_type = car_type.upper()

        with open('data.json', 'r') as fl:
            results = json.load(fl)

        print('This is our wash district', results['district'])
        car_wash_choice = input('\n where you want ? ')
        car_wash_choice = car_wash_choice.upper()
        while True:

            if car_wash_choice == 'ZEYTUN':
                print('\n Our adress is Zeytun Rubinynac 14 working from 9:00 - 19:00 \n')

                if car_type == 'JEEP':
                    print('5000  amd  / if you want to reserve you can call +374-98-29-88-27.')
                    break


                elif car_type == 'SEDAN':
                    print('2500  amd  / if you want to reserve you can call +374-98-29-88-27. ')
                    break


            elif car_wash_choice == 'KOMITAS':
                print('\n Our adress is Komitas Griboedov 20 working 24 hours \n')

                if car_type == 'JEEP':
                    print('6000  amd  / if you want to reserve you can call +374-98-29-88-27. ')
                    break
                elif car_type == 'SEDAN':
                    print('3500  amd  / if you want to reserve you can call +374-98-29-88-27. ')
                    break


            elif car_wash_choice == 'NOR-NORK':
                print('\n Our adress is Nor-Nork Mikoyan 13 working from 9:00 - 23:00 \n')

                if car_type == 'JEEP':
                    print('4000  amd  / if you want to reserve you can call +374-98-29-88-27. ')
                    break
                elif car_type == 'SEDAN':
                    print('2000  amd  / if you want to reserve you can call +374-98-29-88-27.')
                    break


            elif car_wash_choice == 'EREBUNI':
                print('\n Our adress is Erebuni Avanesov 14 working from 9:00 - 22:00 \n')

                if car_type == 'JEEP':
                    print('2500  amd  / if you want to reserve you can call +374-98-29-88-27.')
                    break
                elif car_type == 'SEDAN':
                    print('1500  amd  / if you want to reserve you can call +374-98-29-88-27.')
                    break
        break
    else:
        print('See you next time')
        break