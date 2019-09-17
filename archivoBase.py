class archivoBase(object):
    name = ""

    def __init__(self, name):
        self.name = name

    def carga():
        try:
            archivo = open(self.name + ".txt","a")
            r = []
            while(archivo.readline()):
                lista=[]
                lista.append(archivo.readline())
                r.append(lista)
            archivo.close()
            return(r)
        except IOError:
            print("archivo no encontrado")
            

        ##print(type(r))
        ##archivo.write("\n" + input())

    '''Aqui vamos a poner la escritura sobre el fichero de un objeto de tipo
    base de datos, tambien vamos a tener que recuperar toda la base de datos
    de el fichero'''

    def recuperaArchivo(self, Base_de_Datos):
        pass

        '''funcion que nos hace imprimir en un fichero:
        accedemos a los atributos del objeto base de datos y los vamos escribiendo
        dentro de nuestro archivo txt mediante open() y despues debemos de con write()
        '''
        def escribeArchivo(lista):
            pass
