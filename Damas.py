#Estefania Sanchez Trejo

def optimo(matriz, fila, columna, N):
    for i in range(fila):
        if matriz[i] == columna or \
           matriz[i] - i == columna - fila or \
           matriz[i] + i == columna + fila:
            return False
    return True

def print_matriz(matriz):
    
    for fila in matriz:
        print(' '.join(['O' if c == fila else 'x' for c in range(N)]))
    print()

def resolve_nq(N):
    matriz = [-1] * N
    return resolve_q(matriz, 0, N)

def resolve_q(matriz, fila, N):
    if fila == N:
        print("\nSolucion")
        print_matriz(matriz)
        return True

    solution_true = False
    for columna in range(N):
        if optimo(matriz, fila, columna, N):
            matriz[fila] = columna
            solution_true = resolve_q(matriz, fila + 1, N) or solution_true
            matriz[fila] = -1  # Backtrack

    return solution_true

if __name__ == "__main__":
    N = int(input("Ingrese el tamaño del tablero: "))   

    for i in range(N):
        for j in range(N):
            print("x", end=" ")
        print( )

    fila = int(input("Ingrese la fila de la primera reina: "))
    columna = int(input("Ingrese la columna de la primera reina: "))
    
    col = columna - 1
    fil = fila - 1
    
    if fil < 0 or fil >= N or col < 0 or col >= N:
        print("Posición de la primera reina no válida.")
    else:
        matriz = [-1] * N
        matriz[fil] = col

        if not resolve_q(matriz, fil + 1, N):
            print("No se encontró ninguna solución.")
