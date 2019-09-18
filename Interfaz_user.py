def guardar_menu():
	guarda = archivoBase()
	guarda.escribeArchivo(base.lista)
	print("Base de datos guardada con éxito")
	menu_principal()

def insertar_menu():
	print("Por favor ingresa el registro que quieres ingresar: \n")
	r = input()
	j = base.insertar_registro(r)
	if j :
		print("Registro insertado con éxito\n")
		menu_principal()
	else:
		print("Ocuriió un error al insertar el registro: \n")

def insertar_menu_aux():
	print("Elige una opción: \n")
		print("1. Volver a insertar \n")
		print("2. Salir\n")
		p = int(input())
		if p == 1:
			insertar_menu()
		elif p == 2:
			menu_principal()
		else:
			print("Por favor ingresa una opción válida")
			insertar_menu_aux()

def modificar_menu():
	print("Ingresa el registro que quieres modificar\n")
	s = input()
	print("Por favor ingresa los nuevos valores\n")
	t = input()
	h = base.modificar_registro(s,t)
	if h == -1:
		modificar_menu_aux()
	else: 
		print("Elemento modificado con éxito\n")
		menu_principal()

def modificar_menu_aux():
	print("Elige una opción: \n")
		print("1. Volver a modificar \n")
		print("2. Salir\n")
		p = int(input())
		if p == 1:
			modificar_menu()
		elif p == 2:
			menu_principal()
		else:
			print("Por favor ingresa una opción válida")
			modificar_menu_aux()

def eliminar_menu():
	print("Por favor escribe el registro para eliminar: \n")
	u = input()
	h = base.eliminar_registro(u)
	if h == -1:
		buscar_menu_aux()
	else: 
		print("Elemento eliminado con éxito\n")
		menu_principal()

def eliminar_menu_aux():
	print("Elige una opción: \n")
		print("1. Volver a eliminar \n")
		print("2. Salir\n")
		p = int(input())
		if p == 1:
			eliminar_menu()
		elif p == 2:
			menu_principal()
		else:
			print("Por favor ingresa una opción válida")
			eliminar_menu_aux()

def buscar_menu_aux():
	print("Elige una opción: \n")
		print("1. Volver a buscar \n")
		print("2. Salir\n")
		p = int(input())
		if p == 1:
			buscar_menu()
		elif p == 2:
			menu_principal()
		else:
			print("Por favor ingresa una opción válida")
			buscar_menu_aux()

def buscar_menu():
	print("Por favor escribe una columna para buscar: \n")
	for i in range(len(base.nombres)):
		print(base.nombres[i])
	u = input()
	print("Ingresa un valor para buscar\n")
	s = input()
	h = base.buscar_registro(u,s)
	if h == -1:
		buscar_menu_aux()
	else:
		k = ""
		for i in range(len(h)):
			for l in i:
				k += h[l]
			print(k)
		menu_principal()


def menu_principal():
	print("Por favor elige una opción:\n")
	print("1. Buscar en la base de datos")
	print("2. Eliminar registro")
	print("3. Modificar registro")
	print("4. Insertar registro")
	print("5. Guardar Base de datos")
	print("6. Regresar al menú anterior")
	print("7. Salir")
	c = int(input())
	if c == 1:
		buscar_menu()
	elif c == 2:
		eliminar_menu()
	elif c == 3:
		modificar_menu()
	elif c == 4:
		insertar_menu()
	elif c == 5:
		guardar_menu()
	elif c == 6:
		main_aux_1()
	elif c == 7:
		sys.exit()
	else:
		print("POr favor ingresa una opción válida\n")
		menu_principal()

def menu_crear():
	print("Por favor ingresa el NOMBRE para la base de datos\n")
	name = input()
	print("Por favor ingresa el NÚMERO de columnas que deseas\n\n")
	x = int(input())
	nombres = []
	k = 1
	while x > 0:
		print("Por favor ingresa el NOMBRE de la columna " + k + "\n\n")
		y = input()
		nombres.append(y)
		x -= 1
		k += 1
	crear(nombres, name, x)
	print("¡Base de datos creada con éxito!\n")
	menu_principal()

def crear(lista, name, x):
	base = Base_de_Datos(nombres, [])

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
	lista = cargar(z)
	if lista:
		print("¡Base de datos cargada con éxito!\n")
		menu_principal()
	else:
		aux_cargar()

def cargar(name):
	archivo = archivoBase(name)
	lista = archivo.carga()
	if lista == -1:
		return -1
	else:
		lista_1 = archivo[1::]
		sort(lista_1)
		base = Base_de_Datos(lista[0], lista_1)
		return lista_1
	

def checar_opcion_1(z):
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