#Realiza una funcion que permita obtener el maximo de 3 numeros

a = 10
b = 20
c = 30

print ""
print "Mayor de 3 de numeros"
print "Los numeros son: ", a, b, c
print ""
if a > b and a > c:
	print "El mayor es: ", a

else: 
	if b > a and b > c:
		print "El mayor es: ", b
	else:
		print "El mayor es: ", c

print ""
print "Programa Finalizado"
