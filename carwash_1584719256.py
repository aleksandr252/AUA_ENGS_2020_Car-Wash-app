import random as r
import json


def start():

	global car_wash_choice
	global car_type
	global people_choice

	print('\n Our company present you Car wash \n') 

	
	while True:
		people_choice = input('if you want to wash your car input yes(y) or no ') == 'y' 	
		
		if people_choice:
			
			while True:
				car_wash_choice = input('\n We have four car wash where you want to wash your car Zeytun, Komitas, Nor-Nork, Erebuni? ')
				car_wash_choice = car_wash_choice.upper()
				district = ['ZEYTUN', 'KOMITAS', 'NOR-NORK', 'EREBUNI']
				
				if car_wash_choice in district:
					break
				else:
					print('\nIncorrect input')	

			while True:
					car_type = input('\n Is your car Jeep or Sedan ')
					car_type = car_type.upper()
					cars = ['JEEP', 'SEDAN']	
					
					if car_type in cars:
						break
					else:
						print('\n Incorrect input')
			break			
		else:
			print('\n Always ready to help you when you need it \n')
			return True				
				
	
def cod():
	global cod
	
	cod = []
	your_letters='abcdefghifvwqzxp1234567890'
	for i in range(1,5):
		x = r.choice(your_letters)
		cod.append(x)
	cod = "".join(cod)


def choice():

	while True:
		if car_wash_choice == 'ZEYTUN':
			print('\n Our adress is Zeytun Rubinynac 14 working from 9:00 - 19:00 \n')
			
			if car_type == 'JEEP':
				print('5000  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod: ',cod)
				break
			
			elif car_type == 'SEDAN':
				print('2500  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break

		
		elif car_wash_choice == 'KOMITAS':
			print('\n Our adress is Komitas Griboedov 20 working 24 hours \n')
			
			if car_type == 'JEEP':
				print('6000  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break
			elif car_type == 'SEDAN':
				print('3500  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break

		
		elif car_wash_choice == 'NOR-NORK':
			print('\n Our adress is Nor-Nork Mikoyan 13 working from 9:00 - 23:00 \n')
			
			if car_type == 'JEEP':
				print('4000  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break
			elif car_type == 'SEDAN':
				print('2000  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break

		
		elif car_wash_choice == 'EREBUNI':
			print('\n Our adress is Erebuni Avanesov 14 working from 9:00 - 22:00 \n')
			
			if car_type == 'JEEP':
				print('2500  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break
			elif car_type == 'SEDAN':
				print('1500  amd  / if you want to reserve you can call +374-98-29-88-27. This is your cod:',cod)
				break
	
														
def data():

	file_name = 'car.json'
	json_data = {'district': car_wash_choice,
				'cartype': 	car_type,
				'cod': cod
	}
	my_data = []
	my_data.append(json_data)

	with open(file_name, 'w', encoding = 'utf-8') as f:
		json.dump(my_data, f, ensure_ascii = False)


def get_data():
	
	file_name = 'car.json'
	with open(file_name) as fl:
		results = json.load(fl)

	for result in results:

		print('\n District -',result['district'])
		print('\n Car type -',result['cartype'])
		print('\n Your cod -',result['cod'])

def end():
	while True:
		if start():
			break
		cod()
		choice()
		data()
		get_data()
		break

end()

