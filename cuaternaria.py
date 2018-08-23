num_preguntas = 0

def busquedaCuaternariaV2(vector, elemento, inicio, final):
    while final >= 0:
        p1 = int(inicio + ((final - inicio) / 4))
        p2 = int(inicio + ((final - inicio) / 2))
        p3 = int(inicio + (3*(final - inicio) / 4))

        if vector[p1] == elemento:
            actualizar_contador(1)
            return p1
        elif vector[p2] == elemento:
            actualizar_contador(2)
            return p2
        elif vector[p3] == elemento:
            actualizar_contador(3)
            return p3
        
        # Se incrementa el numero de preguntas a 3, ya que pregunto en las 3 partes del vector y no lo encontro.
        actualizar_contador(3)

        if inicio == final or inicio > final:
            # Quiere decir que ya acorralo lo mas que pudo al elemento y no lo encontro.
            return None
        elif vector[p1] < elemento:
            return busquedaCuaternariaV2(vector, elemento, inicio, p1 - 1)
        elif vector[p2] < elemento:
            return busquedaCuaternariaV2(vector, elemento, p1 + 1, p2 - 1)
        elif vector[p3] < elemento < vector[p2]:
            return busquedaCuaternariaV2(vector, elemento, p2 + 1, p3 - 1)
        else:
            return busquedaCuaternariaV2(vector, elemento, p3 + 1, final)

def actualizar_contador(preguntas):
    global num_preguntas
    num_preguntas += preguntas

if __name__ == '__main__':
    #     0   1   2   3   4    5   6   7   8   9   10  11  12  13  14  15  16  17 18 19 20
    A = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
    
    nro_a_buscar = int(input('Inserte el elemento a buscar: '))
    valor_encontrado = busquedaCuaternariaV2(A, nro_a_buscar, 0, len(A))

    if valor_encontrado:
        print("Encontrado en la posicion: ", valor_encontrado)
        print("Preguntas: ", num_preguntas)
    else:
        print("Elemento no encontrado")
        print("Preguntas: ", num_preguntas)