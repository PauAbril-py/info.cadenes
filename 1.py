cyan = "\033[0;36m"
bright_red = "\033[0;91m"
bright_white = "\033[0;97m"

b=0

print(cyan+"Introdueix"+bright_white+" nom de mascota")

while True:	
	a = input()

	if a[1] == a[-2] and a[0] == a[-1]:
		print("Nom divertit")
		b=0
	else :
		print("Ets un avorrit, el nom no mola")
		b = b+1
	
	if b == 2:
		print("No tens gens d'originalitat."+bright_red+" No pots tenir gos, no pots sortir al carrer. Adéu!")