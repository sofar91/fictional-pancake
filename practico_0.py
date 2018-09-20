# Pre: Recibe dos palabras previamente inicializadas.

# Post: Devuelve la cantidad de letras que suman ambas palabras.
palabra_1 = input('Ingrese una palabra')
palabra_2 = input('Ingrese otra palabra')
def sumarLetras(palabra1, palabra2):

    a = len(palabra1)

    b = len(palabra2)

    sumadeletras = a + b



    return sumadeletras

print(sumarLetras(palabra_1, palabra_2))



# Pre: Recibe dos palabras previamente inicializadas.

# Post: Devuelve true en caso de que la palabra uno sea mas larga o de igual

# longitud que la dos, false en caso contrario.
pal1 = input('Ingrese una palabra')
pal2 = input('Ingrese otra palabra')
def determinarPalabraMasLarga(palabra1, palabra2):

    if len(palabra1) < len(palabra2):

        palabralarga = False

    else:

        palabralarga = True



    return palabralarga

print(determinarPalabraMasLarga(pal1,pal2))




# Pre: Recibe tres valores previamente inicializados: horas, minutos y segundos.

# Post: Devuelve la duracion en segundos del intervalo de tiempo que surge de la suma de la duracion

# en segundos de los tres parametros. EJ: horas: 1, minutos: 3, segundos: 117 devuelve: 3897

hora = input('Ingrese la hora')
minuto = input('Ingrese los minutos')
segundo = input('Ingrese los segundos')

def cantidadDeSegundos(horas, minutos, segundos):

    h = (int(horas) * 3600)

    h = (int(minutos) * 60) + int(h)

    h = int(segundos) + int(h)

    return h

print(cantidadDeSegundos(hora,minuto,segundo))





# Pre: Recibe un numero previamente inicializado.

# Post: Devuelve True si el numero es par, False en caso contrario.
num= input('Ingrese un numero')

def esPar(numero):

    if ((int(numero)% 2)== 0) :

        return True

    else:

       return False


print(esPar(num))

# Pre: Recibe tres numeros previamente inicializados.

# Post: Devuelve el mayor producto entre dos de ellos

# EJ: Si recibe (5,3,8), debe devolver 40.



numeroUno = int(input ('Ingrese un Numero'))

numeroDos = int (input ('Ingrese otro Numero'))

numeroTres = int (input ('Ingrese un ultimo numero'))

def mayorProducto(numeroUno, numeroDos, numeroTres):

    producto1= numeroUno*numeroDos

    producto2= numeroUno*numeroTres

    producto3= numeroDos*numeroTres



    if producto1 >= producto2 and producto1 >= producto3:

        return producto1

    elif producto2 >= producto1 and producto2 >= producto3:

        return producto2

    else:

        return producto3


print(mayorProducto(numeroUno,numeroDos,numeroTres))
