
def error():
    print('_____________Numeros, por favore______________')         #comentarios para cuando releea el código xd
    
crear_diccionario={}         #diccionario

while True:
    print ('+__________________________ __ __ ____________________________+')
    print ('Bienvenido a la tienda virtual de accesorios,soul!')
    print ('Entre nuestras opciones hay anillos,collares y más, totalmente de calidad!/.provenientes de china. *cough,cough*')
    print ('Por favor, seleccione entre las opciones:')
    print ('_._._._._._._._._._._._')
    inicio=print (f'{1}. Ingresar items. \n{2}. Ver los items de la lista. \n{3}. Ver el total. \n{4}. Eliminar un item de su lista. \n{5}. Eliminar todos los items de su lista.')
    print ('_._._._._._._._._._._._')
    print ('+__________________________ __ __ ____________________________+')
    try:
        opciones= int (input ('seleccione un número: ')) #mucho texto, ya sé, mi solución fue más strings
    except ValueError:
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
                    error()     #no niego que cuando aprendes a usar algo no lo sueltas
                    continue
                crear_diccionario[item]= precio         #determina [key]=valor del diccionario --> crear_diccionario
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
                    keys_diccionario=list(crear_diccionario.keys())  #keys muestra las keys de los values del diccionario
                    for i in enumerate (keys_diccionario,start=1):   #(iterable: Iterable, start: int = 0) -> enumerate
                        print (f'{i}.{item}')                        #Imprime num. item en lista
                    try:
                        caso4_elección=int(input('seleccione uno por uno el item que desea eliminar, o escriba 0 si desea volver al inicio: '))
                        if caso4_elección==0:
                            break
                    except ValueError:
                        error()
                        continue                                 #(se elimina 1 ya que la computadora cuenta índices desde cero 0,1,2 etc.)>>evita que se elimine el equivocado, ya que para la computadora 1 es el 2do y el 1er número en el diccionario es 0)
                    indice_items=caso4_elección-1                   #Tuve que buscar solución:"igualar el índice de los items de {crear diccionario}-1,"
                    if 0<= indice_items< len(keys_diccionario):        # len devuelve el número de items en un contenedor
                        caso4_elección=keys_diccionario[indice_items]    #numero ingresado_usuario == a key [índice de los items]
                    del crear_diccionario[caso4_elección]              #delete
                    print(f'Se eliminará el item {caso4_elección}')
                
        case 5:
            while True:
                print ('Vaciar lista!')
                if not crear_diccionario:
                    print ('Su lista ya está vacía.')
                    break
                si_o_no=str(input('Seguro que desea vaciar su lista? y/n: ')).lower().strip()   
                if si_o_no.isdigit() or si_o_no=="":                            #isdigit aah sh, here we go again
                    print ('Y o N, Por favor.Vuelva a intentarlo')              #yeeeeei
                    continue
                if si_o_no=='y':
                    crear_diccionario.clear()
                    continue
                elif si_o_no=='n':
                    print ('Eso estuvo cerca! Volvamos al inicio...')
                    break
        case _:
            print('Por favor, un número válido.')

#intento a ver si funciona Github.
#ya aprendí a hacer push xd