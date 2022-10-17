import random
import math
import time


def generar_lista(n: int, r: int) -> list:
    """
    Argumentos :
        n: int - n es un número impar
        r: int - r >= 0
    Retorna:
        list - lista con n elementos sacados al azar desde el
        intervalo [-r, r] de números enteros
    """
    L = []
    for i in range(0, n):
        L.append(random.randint(-r, r))
    return L


def mediana(L: list) -> int:
    """
    Argumentos :
        L: list - lista de números enteros
    Retorna:
        int - mediana de la lista L, calculada ordenando L
    """
    O = L.copy()
    O.sort()
    return O[len(O) // 2]


def mediana_aleatorizado(L: list) -> int:
    """
    Argumentos :
        L: list - lista de números enteros
    Retorna:
        int - mediana de la lista L, si el algoritmo aleatorizado
        retorna un número entero. Si el algoritmo aleatorizado no
        logra calcular la mediana retorna None.
    """
    if len(L) < 2001:
        print(mediana(L))
    else:
        R = []
        for i in range(0, math.ceil(len(L) ** (3 / 4))):
            R.append(random.choice(L))
        R.sort()
        d = R[math.floor(0.5 * (len(L) ** (3 / 4)) - len(L) ** (1 / 2))]
        u = R[math.floor(0.5 * (len(L) ** (3 / 4)) + len(L) ** (1 / 2))]
        S = []
        m_d = 0
        m_u = 0
        for i in range(0, len(L)):
            if d <= L[i] and L[i] <= u:
                S.append(L[i])
            elif L[i] < d:
                m_d = m_d + 1
            else:
                m_u = m_u + 1
        if (
            m_d > len(L) // 2
            or m_u > len(L) // 2
            or len(S) > 4 * math.floor(len(L) ** (3 / 4))
        ):
            return
        else:
            S.sort()
            return S[len(L) // 2 - m_d]


if __name__ == "__main__":
    largo = 20000001
    rango = 300000
    L = generar_lista(largo, rango)
    t1 = time.time()
    rM = mediana(L)
    t2 = time.time()
    rMA = mediana_aleatorizado(L)
    t3 = time.time()
    print(f"Largo de la lista: {largo}")
    print(f"Rango de los elementos en la lista: [-{rango},{rango}]")
    print(
        f"Resultado algoritmo basado en ordenación: {rM}, tiempo: {t2-t1:.2f} segundos"
    )
    print(f"Resultado algoritmo aleatorizado: {rMA}, tiempo: {t3-t2:.2f} segundos")
