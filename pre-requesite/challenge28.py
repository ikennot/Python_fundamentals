import math;


def bmi_calculator(height,weight):
	bmi = weight / (height ** 2);

	if bmi < 18.5:
		return 'underweight';
	elif bmi >=18.5 or bmi <=24.9:
		return 'normal';
	else:
		return 'overweight';



height = float(input('Enter your height : '));
width = float(input('Enter your weight : '));

bmi = bmi_calculator(height,width);

print('Your BMI result : '+bmi);


	