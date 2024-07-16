'''insertarJugada
DESCRIPCION
    Inserta las jugadas en el tablero de juego

PARAMETROS
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
    jugada      Indice de la casilla en la que se desea insertar la jugada
    jugador     Simmbolo del jugador que puede ser 'x' o 'o'

'''
def insertarJugada(tablero,jugada,jugador):

    if verificarTablero(tablero,jugada):
        tablero[jugada-1] = jugador
    else:
        print("ERROR : Casilla no valida, escoge otra casilla por favor.")

'''imprimirTablero
DESCRIPCION
    Imprime el tablero de juego

PARAMETROS
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
'''
def imprimirTablero(tablero):

    separador = "-----------------"
    linea = ""

    for casilla in range(0,9,1):
        
        if (casilla+1)%3 == 0:
            
            # Ultima casilla de la linea
            linea = linea + "  " + tablero[casilla]
            print(linea)

            # Impresion del separador
            if casilla+1 != 9:
                print(separador)
            
            linea = ""

        else :
            # Creacion de la linea a partir de las casillas
            linea = linea + "  " + tablero[casilla] + "  |"        
'''verificarTablero
DESCRIPCION
    Verifica que la casilla este disponible

PARAMETROS
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
    jugada      Indice de la casilla en la que se desea insertar la jugada

RETORNO
    disponible(True)     Si la casilla esta disponible
    ocupado(False)  Si la casilla no esta disponible
'''
def verificarTablero(tablero,jugada):

    disponible = True
    ocupado = False

    # Verifica si el indice que indica la jugada esta disponible
    if(tablero[jugada-1] == str(jugada)):
        return disponible
    
    return ocupado

'''inicializarTablero
DESCRIPCION
    Inicializa los indices de las casillas del tablero

PARAMETROS
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
'''
def inicializarTablero(tablero):
    for casilla in range(0,9,1):
        tablero.append(str(casilla + 1))

'''verificarGanador
DESCRIPCION
    Verifica si el jugador indicador indicado en los parametros es ganador.
PARAMETROS
    jugador     Simmbolo del jugador que puede ser 'x' o 'o'
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
RETORNO
    victoria(False) El jugador no ha ganado
    victoria(True)  El jugador ha ganado
'''
def verificarGanador(tablero,jugador):
    victoria = False
    combinaciones = {1:[4,5,2],2:[5],3:[5,6],4:[5],7:[8]} #combinaciones ganadoras

    for clave in combinaciones:
        valores = combinaciones[clave]

        for valor in valores:
            #Comprobar si la primera casilla de la combinacion ganadora es del jugador
            casilla = clave-1
            if tablero[casilla] == jugador:
                #Comprobar si la segunda casilla de la combinacion ganadora es del jugador
                casilla = valor-1
                if (tablero[casilla] == jugador):
                    #Comprobar si la tercera casilla de la combinacion ganadora es del jugador
                    casilla = valor + (valor-clave) - 1 # El -1 es por que los indices de la lista empiezan en 0
                    if (tablero[casilla] == jugador):
                        victoria = True
                        return victoria
    return victoria

'''buscarCasillasVacias
DESCRIPCION
    Busca los indices de las casillas que  estan vacias
PARAMETROS
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
RETORNO
    casillas_vacias     Lista con los indices de las casillas vacias del tablero
'''
def buscarCasillasVacias(tablero):
    casillas_vacias = []

    for casilla in tablero:

        if(casilla.isdigit()):
            casillas_vacias.append(int(casilla))

    return casillas_vacias

'''verificarEmpate
DESCRIPCION
    Predice si la partida terminara en empate. Esto lo hace a partir de probar las posibles jugadas futuras de un solo jugador.
PARAMETROS
    tablero     Lista con los valores del tablero. Puede contener numeros que indican el indice de la casilla
                que esta vacia o el valor de la jugada 'x' o 'o'
    jugador     Simmbolo del jugador que puede ser 'x' o 'o'
RETORNO
    empate(True)    No hay posibilidad de que el jugador indicado pueda ganar
    empate(False)   Si hay posibilidad de que el jugador indicado pueda ganar
'''
def verificarEmpate(tablero,jugador):
    empate = True
    tablero_copia = tablero.copy()
    casillas_vacias = buscarCasillasVacias(tablero_copia)

    for casilla in casillas_vacias:
        
        # Rellenamos la casilla vacia
        tablero_copia[casilla-1] = jugador

        # Probamos si en la casilla rellenada, el jugador puede ganar
        if(verificarGanador(tablero_copia,jugador) == True):
            empate = False
            return empate
        
        # Borramos la casilla rellenada
        tablero_copia[casilla-1] = casilla
    
    return empate

def main():

    tablero = []
    inicializarTablero(tablero)
    imprimirTablero(tablero)

    insertarJugada(tablero,5,'x')
    imprimirTablero(tablero)
    insertarJugada(tablero,6,'x')
    print(verificarEmpate(tablero,'x'))

    

# Inicializar main
if __name__ == "__main__":
    main()
