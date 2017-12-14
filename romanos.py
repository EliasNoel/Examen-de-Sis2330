import math
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
decimales=[]
romanos=[]
baseocho=[]
converted_string = ""
base=8
while True:
	valor=int(input("Ingresar valor (0 para finalizar):"))
	if(valor==0): break
	decimales.append(valor)
	#convertir valor a base 8
	converted_string = ""
	currentnum = valor
	while currentnum:
		mod = currentnum % base
		currentnum = currentnum // base
		converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
	baseocho.append(converted_string)
	#fin de convertir valor base 8
	N=valor
	u= N % 10
	d=int(math.floor(N/10))%10
	c=int(math.floor(N/100))
	if(N>=100):
		romanos.append(Centena[c]+Decena[d]+Unidad[u])
	else:
		if(N>=10):
			romanos.append(Decena[d]+Unidad[u])
		else:
			romanos.append(Unidad[N])
	  
print(decimales)
print(romanos)
print(baseocho)