import os

class ArbolBinario:
	def __init__(self,objetoRaiz):
		self.clave = objetoRaiz
		self.hijoIzquierdo = None
		self.hijoDerecho = None
	def insertarIzquierdo(self,nuevoNodo):
		if self.hijoIzquierdo == None:
			self.hijoIzquierdo = ArbolBinario(nuevoNodo)
		else:
			t = ArbolBinario(nuevoNodo)
			t.hijoIzquierdo = self.hijoIzquierdo
			self.hijoIzquierdo = t
	def insertarDerecho(self,nuevoNodo):
		if self.hijoDerecho == None:
			self.hijoDerecho = ArbolBinario(nuevoNodo)
		else:
			t = ArbolBinario(nuevoNodo)
			t.hijoDerecho = self.hijoDerecho
			self.hijoDerecho = t
	def obtenerHijoDerecho(self):
		return self.hijoDerecho
	def obtenerHijoIzquierdo(self):
		return self.hijoIzquierdo
	def asignarValorRaiz(self,obj):
		self.clave = obj
	def obtenerValorRaiz(self):
		return self.clave

def menu(string):
	
	r = ArbolBinario('a')
	print(string)
	opc = int(input('\nElige una opcion: '))
	while(opc!=0):
		if(opc==1):
			print('Valor raiz: ',r.obtenerValorRaiz())
		elif(opc==2):
			print('Insertar hijo izquierdo!')
			valor = input('Inserte nombre del hijo izquierdo: ')
			r.insertarIzquierdo(valor)
		elif(opc==3):
			print(r.obtenerHijoIzquierdo())
			print('Valor del hijo Izquierdo: ',r.obtenerHijoIzquierdo().obtenerValorRaiz())
		elif(opc==4):
			print('Insertar hijo derecho!')
			valor = input('Inserte nombre del hijo derecho: ')
			r.insertarDerecho(valor)
		elif(opc==5):
			print(r.obtenerHijoDerecho())
			print('Valor del hijo derecho: ',r.obtenerHijoDerecho().obtenerValorRaiz())
		elif(opc==6):
			print('Actualizar valor del hijo\n[1]HIjo izquierdo\t[2]Hijo derecho')
			hijo = int(input('Escoga hijo a actualizar valor: '))
			valorAc = input('Introduzca nombre nuevo: ')
			if(hijo==1):
				r.obtenerHijoIzquierdo().asignarValorRaiz(valorAc)
				print('Valor del hijo Izquierdo: ',r.obtenerHijoIzquierdo().obtenerValorRaiz())
			elif(hijo==2):
				r.obtenerHijoDerecho().asignarValorRaiz(valorAc)
				print('Valor del hijo Derecho:',r.obtenerHijoDerecho().obtenerValorRaiz())	
		elif(opc==0):
			print('Adios')
		else:
			os.system('clear')
			print(string)
		opc = int(input('\nEscoge otra opcion:'))

		
def  main():
	
	string = '\t\tMenu\n[1]Obtener valor Raiz\t[2]Insertar Izquierdo\t[3]Obtener Izquierdo\t[4]Insertar Derecho\t[5]Obtener Derecho\t[6]Actualizar valor\t[0]Salir'
	menu(string)
	
	
main()
