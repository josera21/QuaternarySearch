num_preguntas = 0
num_preguntas_no_exi = 0

def busquedaBinaria (vector, inicio, fin, num_a_buscar):
    global num_preguntas, num_preguntas_no_exi
    if (inicio == fin): return vector[inicio] == num_a_buscar
    centro = ((fin - inicio) // 2) + inicio
    print(centro)
    num_preguntas += 1 
    
    if (num_a_buscar > vector [centro]):
        print('izquierda')
        num_preguntas_no_exi += 1
        return busquedaBinaria (vector, inicio, centro - 1, num_a_buscar)
    
    elif (num_a_buscar < vector[centro]):
        print('derecha')
        num_preguntas_no_exi += 1
        return busquedaBinaria (vector, centro + 1, fin, num_a_buscar)
    
    else: return True

def comenzarBusqueda (vector, num_a_buscar):
    if (vector == None) or (vector == []):
        return False
    
    else: return busquedaBinaria (vector, 0, len (vector) - 1, num_a_buscar)

if __name__ == '__main__':
    A = [100 , 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
    print(comenzarBusqueda(A, 29))
    print('preguntas: ', num_preguntas)
    print('preguntas no exitosas: ', num_preguntas + 1)