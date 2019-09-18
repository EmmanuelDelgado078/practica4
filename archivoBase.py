class archivoBase(object):
    name = ""

    def __init__(self, name):
        self.name = name
    
    ''' funcion que nos va a ayudar a recuperar todo lo que hay dentro del archivo'''
    def carga(cadena):
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
            return -1
            

        ##print(type(r))
        ##archivo.write("\n" + input())

        '''funcion que nos hace imprimir en un fichero:
        accedemos a los atributos de la lista y los vamos escribiendo
        dentro de nuestro archivo txt mediante open() y despues debemos de con write()
        '''
        def escribeArchivo(lista):
            for i in lista:
                archivo = open(self.name, "w")
                archivo.write("\n" + i)
            archivo.close()