from colorama import init , Fore , Back , Style	

#intialize
def color_init():
	init()
	
color_init()

#use this when you print 
def printRed(_str,_boolnewline=False):
	if _boolnewline == True:
		print(Fore.RED +_str + Style.RESET_ALL)
	else:
		print(Fore.RED +_str + Style.RESET_ALL,end="")
	
def printYellow(_str,_boolnewline=False):
	if _boolnewline == True:
		print(Fore.YELLOW +_str + Style.RESET_ALL)
	else:
		print(Fore.YELLOW +_str + Style.RESET_ALL,end="")

def printGreen(_str,_boolnewline=False):
	if _boolnewline == True:
		print(Fore.GREEN +_str + Style.RESET_ALL)
	else:
		print(Fore.GREEN +_str + Style.RESET_ALL,end="")
def printBlue(_str,_boolnewline=False):
	if _boolnewline == True:
		print(Fore.BLUE +_str + Style.RESET_ALL)
	else:
		print(Fore.BLUE +_str + Style.RESET_ALL,end="")


def printBlueGreen(_str,_boolnewline=False):
	if _boolnewline == True:
		print(Fore.CYAN +_str + Style.RESET_ALL)
	else:
		print(Fore.CYAN +_str + Style.RESET_ALL,end="")

def printPurple(_str,_boolnewline=False):
	if _boolnewline == True:
		print(Fore.MAGENTA +_str + Style.RESET_ALL)
	else:
		print(Fore.MAGENTA +_str + Style.RESET_ALL,end="")
