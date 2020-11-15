a=input("Escriu una frase\n").title()

print(a)

b=len(a.split())

print("\nHi han",b,"paraules.")

c=len(a)-a.count(" ")

print("Hi han",c,"caracters.")

d=0
for s in a.lower():
	if s in "aeiou": d=d+1

print("Hi han",d,"vocals")

e=c-d

print("Hi han",e,"consonants")