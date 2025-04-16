
    # mostrar segun criterio
    # entre 12 y 17 años es adolecente 
    # entre 18 y 64 es adulto
    # 65 y mas, es adulto mayor
edad=int(input("ingrese su edad "))
if edad<12:
    print ("usted es un niño")
elif edad>=12 and edad<18: 
    print ("usted es adolecente")
elif edad>=18 and edad<65:
    print (" usted es adulto")
else:
    print ("usted es un tatita") 