import random

def banner00():
	print("\n\n")
	print("  █████████  █████                                   ███████████  █████ █████")
	print(" ███░░░░░███░░███                                   ░░███░░░░░███░░███ ░░███ ")
	print("░███    ░░░  ░███████    ██████   ████████   ██████  ░███    ░███ ░░███ ███  ")
	print("░░█████████  ░███░░███  ░░░░░███ ░░███░░███ ███░░███ ░██████████   ░░█████   ") 
	print(" ░░░░░░░░███ ░███ ░███   ███████  ░███ ░░░ ░███████  ░███░░░░░░     ░░███    ")
	print(" ███    ░███ ░███ ░███  ███░░███  ░███     ░███░░░   ░███            ░███    ")
	print("░░█████████  ████ █████░░████████ █████    ░░██████  █████           █████   ") 
	print("░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░░           ░░░░░     ")                                                   
	print("\n\n\n\n")

 
def printBanner():
	chosenFunction = random.randint(0,10)
	switcher = {
		0: banner00,
		1: banner00,
		2: banner00,
		3: banner00,
		4: banner00,
		5: banner00,
		6: banner00,
		7: banner00,
		8: banner00,
		9: banner00,
		10: banner00
	}
	func = switcher.get(chosenFunction, lambda: "\n  Oops something went wrong: \n\n    SharePy!\n\n")
	func()