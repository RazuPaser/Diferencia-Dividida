print ("------- Interpolacion Polinomica (Newton) -------")
print ("Pegueros Pérez Raúl Bernardo")
print ("Metodos Numericos")
print ("Grado de Polinomio")
print ("------------------------------")
n = int(input("Ingrese el grado del polinomio a evaluar: "))+1
# print ("El grado del polinomio es: ", n)
matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n
print ("------------------------------")
print (matriz)
print (vector)
print ("Se necesitan: ",n," puntos")
for i in range(n):
    x = input("Ingrese el valor de x: ")
    y = input("Ingrese el valor de f("+x+"): ")
    vector[i]=float(x)
    matriz[i][0]=float(y)
print ("------------------------------")
print (vector)    
print (matriz)
print ("------------------------------")
for i in range(1,n):
    for j in range(i,n):
        print ("i=",i,"    j=",j)
        print ("(",matriz[j][i-1],"-",matriz[j-1][i-1],")/(",vector[j],"-",vector[j-i],")")
        matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))
        print ("matriz[",j,"][",i,"] = ",(matriz[j][i-1]-matriz[j-1][i-1])/(vector[j]-vector[j-i]))
print ("------------------------------")
for i in range(n):
    print (matriz[i])
print ("------------------------------")
pae = float(input("Ingrese el punto a evaluar: "))
aprx = 0
mul = 1.0
for i in range(n):
    mul = matriz[i][i]
    for j in range(1,i+1):
        mul = mul * (pae - vector[j-1])
    # print (aprx)
    aprx = aprx + mul

print ("------------------------------")
print ("El valor aproximado de f(",pae,") es: ", aprx)