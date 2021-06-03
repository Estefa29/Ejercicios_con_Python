vehiculos={'renault':36000000,'chevrolet':45000,'audi':79000000}

for valor in vehiculos:
    if vehiculos[valor]>1000000:
        print(valor,vehiculos[valor])

# escribir un programa que guarde en un  diccionario los precios de las frutas 

Frutas={'platano':135,'manzana':200,'peras':100,'naranjas':800}
fruta=input('que fruta desea:').title()
kg=float(input('¿cuantos kilos quiere?'))

for fruta in Frutas:
    
    valor=Frutas[fruta]*kg
    print('los kilos solicitados son')
else:
    print(' no se encuentra el producto solicitado')