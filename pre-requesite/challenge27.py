def name_formatter(firstname,lastname):
	return firstname+' '+lastname;


fname = input('Enter your first name : ');
sname = input('Enter yout last name : ');

str = name_formatter(fname,sname);

print('Your name is : '+str);