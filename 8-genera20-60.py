#Programa que imprime la suma de los cubos de n numeros
print "----------------------------------------------------------"
print "-       Programa que genera n numeros entre 20 y 60      -"
print "----------------------------------------------------------"
print ""
print "INTRODUZCA EL NUMERO: "
num = input()
print ""

i = 20
contador = 1
lista = []

while contador<=num:
	
	i += 1
	contador += 1
	lista.append(i)
	if (i==59):
		break
	#print (n)
print ""	
print "Lista de numeros: ", lista

print "---------------------------------------"
print "-       PROGRAMA FINALIZADO           -"
print "---------------------------------------"