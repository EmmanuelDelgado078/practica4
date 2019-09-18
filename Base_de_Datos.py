class Base_de_Datos(object):

	base = Registro()
	nombres = []

	def __init__(self, nombres, base):
		self.nombres = nombres
		self.base.lista = base

	def modificar_registro(s,t):
		s.split(" ")
		indice = base.lista.index(s)
		if s in base.lista:
			base.lista[indice] = t
			return True
		else:
			print("El registro no existe\n")
			

	def insertar_registro(arr):
		arr = arr.split(" ")
		base.lista.append(arr)
		base.lista = sort(base.lista)

	def eliminar_registro(u):
		u = u.split(" ")
		if u in base.lista:
			base.lista.pop(u)
			return True
		else:
			print("El registro que deseas eliminar no existe\n")
			return -1

	def buscar_registro(u,s):
		try:
			indice = nombres.index(u)
			coincidencias = []
			for arr in base.lista:
				if arr[indice] == s
					coincidencias.append(arr)
		except:
			print("La columna ingresada no existe")
			return -1
		