student =input('Are you student ? : ');
age = int(input('What is your age? ? '));

isStudent = (student == ('yes' or 'Yes'));

if isStudent and (age > 10 and age <=60):
	print('Discount granted');
else:
	print('no discount');