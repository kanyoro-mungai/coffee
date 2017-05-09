#make coffee
def makecoffee():
	name = raw_input('name:')

	print('Take a cup')
	print('add hot water')
	print('add cream')
	print('pour coffee into a cup')
	print('add sugar')
	print('stir')
	print('enjoy')
	
	coffee = "Tasty Coffee"
	space = " "
	owner = coffee + space + name

	return owner

def serve_coffee(coffee1):

	print ('Here is your {}'.format(coffee1))

serve_coffee(makecoffee())






