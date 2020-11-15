b=0
c=0

print("Introdueix nom de mascota")

while True:	
	a = input()

	if a.isnumeric() == True:
		if a[1] == a[-2] and a[0] == a[-1] and a[2] == a[-3]:
			print("Capicua numèric plus")
			b=0
			c=c+3
		elif a[1] == a[-2] and a[0] == a[-1]:
			print("Capicua numèric normal")
			b=0
			c=c+2
	elif a.isnumeric() == False:
		if a[1] == a[-2] and a[0] == a[-1] and a[2] == a[-3]:
			print("Capicua de lletres plus")
			b=0
			c=c+4
		elif a[1] == a[-2] and a[0] == a[-1]:
			print("Capicua de lletres")
			b=0
			c=c+3
	else :
		print("Ets un avorrit, el nom no mola")
		b = b+1
	
	if b == 2:
		print("No tens gens d'originalitat. No pots tenir gos, no pots sortir al carrer. Adéu!")