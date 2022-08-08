
import random
import math
import time



def exp(a: int, b: int) -> int:
    """
    Argumentos :
        a: int
        b: int - b >= 0
    Retorna :
        int - a**b
    """
    if b == 0:
        return 1
    else:
        res = 1
        pot = a
        while b > 0:
            if b % 2 == 1:
                res = pot * res
            b = b // 2
            pot = pot * pot
        return res



def exp_mod(a: int, b: int, n: int) -> int:
    """
    Argumentos :
        a: int
        b: int
        n: int - n > 0
    Retorna :
        int - a**b en modulo n
    """
    if b == 0:
        return 1
    elif b > 0:
        res = 1
        pot = a
        while b > 0:
            if b % 2 == 1:
                res = (pot * res) % n
            b = b // 2
            pot = (pot * pot) % n
        return res
    else:
        return exp_mod(inverso(a,n),-b,n)

    

def mcd(a: int, b: int) -> int:
    """
    Argumentos :
        a: int
        b: int - a > 0 o b > 0
    Retorna :
        maximo comun divisor entre a y b,
    """
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a



def alg_ext_euclides(a: int, b: int) -> (int, int, int):
    """
    Argumentos :
        a: int
        b: int - a >= b >= 0 y a > 0
    Retorna :
        (int , int , int) - maximo comun divisor MCD(a, b) entre a y b,
        y numeros enteros s y t tales que MCD(a, b) = s*a + t*b
    """
    r_0 = a
    s_0 = 1
    t_0 = 0
    r_1 = b
    s_1 = 0
    t_1 = 1
    while r_1 > 0:
        r_2 = r_0 % r_1
        s_2 = s_0 - (r_0 // r_1) * s_1
        t_2 = t_0 - (r_0 // r_1) * t_1
        r_0 = r_1
        s_0 = s_1
        t_0 = t_1
        r_1 = r_2
        s_1 = s_2
        t_1 = t_2
    return r_0, s_0, t_0



def inverso(a: int, n: int) -> int:
    """
    Argumentos :
        a: int - a >= 1
        n: int - n >= 2, a y n son primos relativos
    Retorna :
        int - inverso de a en modulo n
    """
    (r, s, t) = alg_ext_euclides(a, n)
    return s % n



def es_potencia(n: int) -> bool:
    """
    Argumentos :
        n: int - n >= 1
    Retorna :
        bool - True si existen numeros naturales a y b tales que n = (a**b),
        donde a >= 2 y b >= 2. En caso contrario retorna False.       
    """
    if n <= 3:
        return False
    else:
        k = 2
        lim = 4
        while lim <= n:
            if tiene_raiz_entera(n, k):
                return True
            k = k + 1
            lim = lim * 2
        return False


    
def tiene_raiz_entera(n: int, k: int) -> bool:
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 2
    Retorna :
        bool - True si existe numero natural a tal que n = (a**k),
        donde a >= 2. En caso contrario retorna False.       
    """
    if n <= 3:
        return False
    else:
        a = 1
        while exp(a,k) < n:
            a = 2*a
        return tiene_raiz_entera_intervalo(n, k, a//2, a)


    
def tiene_raiz_entera_intervalo(n: int, k: int, i: int, j: int) -> bool:
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 2
        i: int - i >= 0
        j: int - j >= 0
    Retorna :
        bool - True si existe numero natural a tal que n = (a**k),
        donde i <= a <= j. En caso contrario retorna False.       
    """
    while i <= j:
        if i==j:
            return n == exp(i,k)
        else:
            p = (i + j)//2 
            val = exp(p,k)
            if n == val:
                return True
            elif val < n:
                i = p+1
            else:
                j = p-1
    return False



def test_primalidad(n: int, k: int) -> bool:
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 1
    Retorna :
        bool - True si n es un numero primo, y False en caso contrario.
        La probabilidad de error del test es menor o igual a 2**(-k),
        y esta basado en el test de primalidad de Solovay–Strassen
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    elif es_potencia(n):
        return False
    else:
        neg = 0
        for i in range(1,k+1):
            a = random.randint(2,n-1)
            if mcd(a,n) > 1:
                return False
            else:
                b = exp_mod(a,(n-1)//2,n)
                if b == n - 1:
                    neg = neg + 1
                elif b != 1:
                    return False
        if neg > 0:
            return True
        else:
            return False


        
def test_miller_rabin(n: int, k: int) -> bool :
    """
    Argumentos :
        n: int - n >= 1
        k: int - k >= 1
    Retorna :
        bool - True si n es un numero primo, y False en caso contrario.
        La probabilidad de error del test es menor o igual a 2**(-k),
        e implementa el test de primalidad de Miller-Rabin.
    """
    if n == 1:
        return False
    elif n==2:
        return True
    elif n%2 == 0:
        return False
    else:
        s = 0
        d = n-1
        while d%2==0:
            s = s + 1
            d = d//2
        num = k//2 + 1
        for i in range(0,num):
            a = random.randint(2,n-1)
            pot = exp_mod(a,d,n)
            if pot != 1 and pot != n-1:
                pasar = False
                for j in range(0,s):
                    pot = (pot*pot) % n
                    if pot == n-1:
                        pasar = True
                        break
                if pasar == False:
                    return False
        return True


    
def generar_primo(l: int) -> int :
    """
    Argumentos :
        l: int - l >= 1
    Retorna :
        int - numero primo con al menos l digitos. La probabilidad de
        error en la generacion es menor o igual a 2**(-100)
    """
    while True:
        primo = random.randint(exp(10,l-1), exp(10,l)-1)
        if test_miller_rabin(primo,100):
            return primo


        
if __name__ == "__main__":
    P = 5943632362508814456797384433006100442712303295066940614569354936549874999082678378231629906729379134167935471382621311620276545251597436711454168850267595109678077983960376792735878876067066338864239372227790339203350191408856924700453890622245349547304896138668552188577288047417779378700982792791819866553113608966810109430765067528429902116607213626746562172730714525439765422832045628189761714003
    Q = 5948532305206754124807034526568653202866615790714581257326259200781183046215133271593709493695066326306188642344623474970917156589328382183408635517678515863592349508921721874016384855821123166737680537740217861149566652056967439689712155308242028846864494656353612317681632254615802412730090202226196256700521991419744087148881094919263518910917691951140424007952761686208616067892053677278599271911
    t1 = time.time()
    rP = test_primalidad(P,100)
    t2 = time.time()
    rQ = test_primalidad(Q,100)
    t3 = time.time()
    rPQ = test_primalidad(P*Q,100)
    t4 = time.time()
    print("P: " + str(rP) + ", tiempo: " + str(t2 - t1) + " segundos") 
    print("Q: " + str(rQ) + ", tiempo: " + str(t3 - t2) + " segundos") 
    print("P*Q: " + str(rPQ) + ", tiempo: " + str(t4 - t3) + " segundos") 
