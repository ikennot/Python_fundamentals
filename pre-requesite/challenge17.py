animals = ['dog','cat','horse','dog','bird','cat','dog'];

animal = input('enter an animal ');

if animal in animals:
	print(animal,'is in the list');
	print('there are',animals.count(animal),'in the list');