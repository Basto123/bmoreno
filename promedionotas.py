# pedir al usuario cantidad de notas
# y generae el promedio de estos

# cant=int(input("ingrese el nunmero de notas"))
# suma=0
# for i in range (cant):
#     print ("ingrese nota",i+1)
#     nota=int(input())
#     # suma+=nota
#     suma=suma+nota
# prom=suma/cant
# print("el promedio es",prom)


# pida la cantidad de alumnos y luego cantidad de notas por alumno
# muestre el promedio de cada uno


cantA=int(input("ingrese el nunmero de alumnos"))

for j in range(cantA):
    cantN=int(input("ingrese el nunmero de notas del alumno",j+1))
    suma=0
    for i in range (cantN):
        print ("ingrese nota",i+1, "del alumno ", j+1 )
        nota=float(input())
        # suma+=nota
        suma=suma+nota
prom=suma/cantN
print("el promedio es",prom)