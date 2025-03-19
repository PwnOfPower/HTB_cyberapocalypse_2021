import codecs

file = open('poc2.txt')

lineas = file.read().splitlines()

for linea in lineas:
	for posicion in range(0,len(linea),2):
		palabra = linea[posicion:posicion+2]
		try:
			print(str(codecs.decode(palabra,'hex'),'utf-8'), end='')
		except:
			print(".", end='')

	print("")
