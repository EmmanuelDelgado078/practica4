def menu_principal():
	print("Por favor elige una opción:\n")
	print("1. Buscar en la base de datos")
	print("2. Eliminar registro")
	print("3. Modificar registro")
	print("4. Guardar Base de datos")
	print("5. Regresar al menú anterior")
	print("6. Salir")


def menu_crear():
	print("Por favor ingresa el NÚMERO de columnas que deseas\n\n")
	x = int(input())
	lista = []
	k = 1
	while x > 0:
		print("Por favor ingresa el NOMBRE de la columna " + k + "\n\n")
		y = input()
		lista.append(y)
		x -= 1
		k += 1
	crear(lista)
	menu_principal()

def aux_cargar():
	print("\n\nEscribe el NÚMERO que corresponda a una opción\n")
	print("1. Volver a intentarlo\n")
	print("2. Crear base de datos\n")
	print("3. Regresar al menú anterior\n")
	print("4. Salir\n")
	y = int(input())
	if y == 1:
		menu_cargar()
	elif y == 2:
		menu_crear()
	elif y == 3:
		main_aux_1()
	elif y == 4:
		sys.exit()
	else:
		print("Por favor ingresa un número válido")
		aux_cargar()

def menu_cargar():
	print("Por favor, introduce el NOMBRE del archivo que deseas cargar\n")
	z = input()
	if not cargar(z):
		print("nombre incorrecto")
		aux_cargar()
	else:
		menu_principal()


def checar_opcion(z):
	if z == 1:
		menu_crear()
	elif z == 2:
		menu_cargar()
	elif z == 3:
		sys.exit()
	else:
		print("Por favor ingresa un número válido")
		main_aux_1()

def main_aux_1():
	print("Por favor ingresa el número que corresponda a la función que quieres utilizar\n\n")
	print("1. Crear una nueva base de datos\n")
	print("2. Cargar base de datos\n")
	print("3. Salir\n")
	z = int(input())
	checar_opcion_1(z)

def main():
	print("\n¡Bienvenido al programa para manejar bases de datos!")
	main_aux_1()

if __name__ == "__main__":
	main()
