ingles = ["i","am","very","tired","jesus","love","you"]
espanol = ["yo","estoy","muy","cansado","jesus","ama","te"]
dicho = raw_input("Ingrese la frase")
lista=dicho.split()
traducido=[]
for i in range(len(lista)):
	traducido.append(ingles[espanol.index(lista[i])])
	
palabra_traducida =' '.join(traducido)
	
print(palabra_traducida)