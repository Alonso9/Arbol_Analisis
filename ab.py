import os

class Pila:
	def __init__(self):
		self.items = []
	def estaVacia(self):
		return self.items == []
	def incluir(self, item):
		self.items.append(item)
	def extraer(self):
		try:
			return self.items.pop()
		except IndexError:
			print("La pila está vacía")
	def inspeccionar(self):
		return self.items[len(self.items)-1]
	def tamano(self):
		return len(self.items)

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


#Incluir la clase para manejo de Pilas y la clase para Árbol Binario
def construirArbolAnalisis(expresionAgrupada):
	listaSimbolos = expresionAgrupada.split()
	pilaPadres = Pila()
	arbolExpresion = ArbolBinario('')
	pilaPadres.incluir(arbolExpresion)
	arbolActual = arbolExpresion
	for i in listaSimbolos:
		if i == '(':
			arbolActual.insertarIzquierdo('')
			pilaPadres.incluir(arbolActual)
			arbolActual = arbolActual.obtenerHijoIzquierdo()
		elif i not in ['+', '-', '*', '/', '^', 'PI', ')']:
			arbolActual.asignarValorRaiz(float(i))
			padre = pilaPadres.extraer()
			arbolActual = padre
		elif i in ['+', '-', '*', '/','^','PI']:
			arbolActual.asignarValorRaiz(i)
			arbolActual.insertarDerecho('')
			pilaPadres.incluir(arbolActual)
			arbolActual = arbolActual.obtenerHijoDerecho()
		elif i == ')':
			arbolActual = pilaPadres.extraer()
		else:
			raise ValueError
	return arbolExpresion
	
#miArbolAnalisis = construirArbolAnalisis("( ( 10 + 5 ) * 3 )")
#print(miArbolAnalisis) # Imprime objeto árbol, no muestra los valores en los nodos
si = '( '
sf = ' )'

ope = si
#print('Importante,ingrese la expresion sin espacios y con todas las llaves!')
exi = input('Ingrese una expresion {ejemplo: 7 + 3}: ')
#print(ope) 
for i in exi:
	#print(i)
	ope += i
	ope += " "
	
ope += sf
print(ope) 
ex2 = "( ( 10 + 5 ) * 3 )"
ex1 = "( ( 7 + 3 ) * ( 5 - 2 ) )"
ex3 = "( 2 ^ 3 )"
ex4 = "( 3 ^ ( 4 / 2 ) )"
ex5 = "PI * 2"
exfinal = ex5
miAborlAnalizis = construirArbolAnalisis(exfinal)
#print('objecto: ',miAborlAnalizis)
	
	
import operator
def evaluar(arbolAnalisis):
	operadores = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv,'^':operator.pow,'PI':operator.mul(2,3.1416)}
	hijoIzquierdo = arbolAnalisis.obtenerHijoIzquierdo()
	hijoDerecho = arbolAnalisis.obtenerHijoDerecho()
	if hijoIzquierdo and hijoDerecho:
		fn = operadores[arbolAnalisis.obtenerValorRaiz()]
		return fn(evaluar(hijoIzquierdo),evaluar(hijoDerecho))
	else:
		return arbolAnalisis.obtenerValorRaiz()
#print(r.obtenerHijoDerecho().obtenerValorRaiz())
#print("Resultado: ",evaluar(miAborlAnalizis))

#print('Preorden')
def preorden(arbol):
	if arbol:
		print(arbol.obtenerValorRaiz())
		preorden(arbol.obtenerHijoIzquierdo())
		preorden(arbol.obtenerHijoDerecho())
#preorden(miAborlAnalizis)

#print('Postorden')
def postorden(arbol):
	if arbol != None:
		postorden(arbol.obtenerHijoIzquierdo())
		postorden(arbol.obtenerHijoDerecho())
		print(arbol.obtenerValorRaiz())

#postorden(miAborlAnalizis)

import operator
def evalPostorden(arbol):
	operadores = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv,'^':operator.pow, 'PI':operator.mul}
	res1 = None
	res2 = None
	
	if arbol:
		res1 = evalPostorden(arbol.obtenerHijoIzquierdo())
		res2 = evalPostorden(arbol.obtenerHijoDerecho())
	if res1 and res2:
		return operadores[arbol.obtenerValorRaiz()](res1,res2)
	else:
		return arbol.obtenerValorRaiz()
		
#print('Inorder')
def inorden(arbol):
	if arbol != None:
		inorden(arbol.obtenerHijoIzquierdo())
		print(arbol.obtenerValorRaiz())
		inorden(arbol.obtenerHijoDerecho())
#inorden(miAborlAnalizis)


def imprimirExpresion(arbol):
	valorCadena = ""
	if arbol:
		valorCadena = '(' + imprimirExpresion(arbol.obtenerHijoIzquierdo())
		valorCadena = valorCadena + str(arbol.obtenerValorRaiz())
		valorCadena = valorCadena + imprimirExpresion(arbol.obtenerHijoDerecho())+')'
	return valorCadena
print('Expresion original: ',imprimirExpresion(miAborlAnalizis))



string = '\t\tMenu\n[1]Obtener Resultado\t[2]Obtener Preorden\t[3]Obtener Inorder\t[4]Obtener Postorden\t[0]Salir'
print(string)
opc = int(input('\nElige una opcion: '))
while(opc!=0):
	if(opc==1):
		print('Expresion:',exfinal)
		print("Resultado: ",evaluar(miAborlAnalizis))
		print('objecto: ',miAborlAnalizis)
	elif(opc==2):
		print('Preorden:')
		preorden(miAborlAnalizis)
	elif(opc==3):
		print('Inorder:')
		inorden(miAborlAnalizis)
	elif(opc==4):
		print('Postorden:')
		postorden(miAborlAnalizis)
	else:
		os.system('clear')
		print(string)
	opc = int(input('\nEscoge otra opcion:'))
