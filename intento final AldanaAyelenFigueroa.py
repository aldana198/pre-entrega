
def error():
    print('_____________Numeros, por favore______________')
    
crear_diccionario={}

while True:
    print ('+__________________________ __ __ ____________________________+')
    print ('Bienvenido a la tienda virtual de accesorios,soul!')
    print ('Entre nuestras opciones hay anillos,collares y más, totalmente de calidad!/.provenientes de china. *cough,cough*')
    print ('Por favor, seleccione entre las opciones:')
    inicio=print (f'{1}. Para ingresar items. \n{2}. para ver los items de la lista. \n{3}. para ver el total. \n{4}. Para eliminar un item de su lista. \n{5}. Para eliminar todos los items de su lista.')
    print ('+__________________________ __ __ ____________________________+')
    try:
            opciones= int (input ('seleccione un número: ')) #mucho texto, ya sé, mi solución fue más strings
    except ValueError:
        print ('Por favor, enserio. YAAAGH')
        error()
        continue
    match opciones:
        case 1:
            while True:
                item=str(input(f'escriba el nombre del item, o {0} si quiere volver al inicio: ')).lower().strip()
                if item=='0':
                    break
                if item.isdigit() or item =="":
                    print ('Escriba el nombre del item, por favor') #Al poner números me lo aceptaba igual así que busqué una forma de evitarlo ;;
                    continue
                try:
                    precio= int (input ('Precio del item: '))
                except ValueError:
                    error() #no niego que cuando aprendes a usar algo no lo sueltas
                    continue
                crear_diccionario[item]= precio
                print (f'Su item {item} se guardó con éxito')
                print ('Sus items actuales son:')
                crear_diccionario.items()
                #me fue imposible agregar más características, iba a ser de ropa, pero no logré hacer que el usuario pudiera crear (diccionario=key:value) con más de un valor, intenté meter listas en diccionarios o hacer una lista de diccionarios creados por usuarios, funcionaba, pero no funcionaba como quería xd
        case 2:
            print ('Ver todos los items!')
            print (f'los items de su lista son: {crear_diccionario.items()}')
        case 3:
            print ('Ver el total de su lista!')
            suma_total_lista=sum(crear_diccionario.values())
            print (f'La suma total de su lista es: ${suma_total_lista}')
            if suma_total_lista==0:
                print ('Parece que no hay items en su lista!')
        case 4:
            while True:
                print ('Su actual lista: ')
                if not crear_diccionario:
                    print ('Ups, parece estar vacío! Nos falta agregar items para poder borrarlos...') #bucle infinito, necesitaba break
                    break
                else:
                    keys_diccionario=list(crear_diccionario.keys()) #keys muestra las keys de los values del diccionario
                    for i in enumerate (keys_diccionario,start=1):   #(iterable: Iterable, start: int = 0) -> enumera cada item segun índice?
                        print (f'{i}.{item}')
                    try:
                        caso4_elección=int(input('seleccione uno por uno el item que desea eliminar: '))
                    except ValueError:
                        error()
                        continue
                    del crear_diccionario[caso4_elección]
                    print(f'Se eliminará el item {caso4_elección}')
                
        case 5:
            print ('Vaciar lista!')
            si_o_no=input('Seguro que desea vaciar su lista? y/n: ')
            if si_o_no=='y':
                crear_diccionario.clear()
                continue
            if si_o_no=='n':
                print ('Eso estuvo cerca! Volvamos al inicio...')
                continue
        case _:
            print('prueba a ver si funca mal o no')

#intento a ver si funciona Github.
