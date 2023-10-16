#Grigorascenco OLEG IF ANUL II
import math

#1.Scrieți un program care să afișeze suma numerelor de la 1 la 100 .
def suma_de_la_1_la_100():
    suma = 0
    for i in range(1, 101):
        suma += i
    print("Suma numerelor de la 1 la 100 este:", suma)

suma_de_la_1_la_100()


#2.Scrieți un program care să determine produsul primelor 10 numere naturale.
def produs_primele_10_naturale():
    produs = 1
    for i in range(1, 11):
        produs *= i
    return produs

rezultat = produs_primele_10_naturale()
print("Produsul primelor 10 numere naturale este:", rezultat)


#3.Scrieți un program care să afișeze primele 20 de numere impare.
def primele_20_numere_impare():
    numar = 1
    numere_impare = []
    
    while len(numere_impare) < 20:
        if numar % 2 == 1:
            numere_impare.append(numar)
        numar += 1

    for numar_impar in numere_impare:
        print(numar_impar)

primele_20_numere_impare()



#4.Determinați cel mai mare divizor comun (CMMD) a două numere întregi citite de la tastatură.
import math

def cmmd_doua_numere():
    numar1 = int(input("Introduceți primul număr întreg: "))
    numar2 = int(input("Introduceți al doilea număr întreg: "))
    
    cmmd = math.gcd(numar1, numar2)
    
    return cmmd

rezultat = cmmd_doua_numere()
print(f"Cel mai mare divizor comun al celor două numere este {rezultat}.")

#5.Scrieți un program care să calculeze factorialul unui număr întreg citit de la tastatură.
def factorial(n):
    if n < 0:
        return "Factorialul nu este definit pentru numere negative."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numar = int(input("Introduceți un număr întreg pentru a calcula factorialul: "))
rezultat = factorial(numar)
print(f"Factorialul lui {numar} este {rezultat}.")

#6.Determinați dacă un număr întreg dat este un număr prim.
def este_numar_prim(numar):
    if numar <= 1:
        return False
    elif numar <= 3:
        return True
    elif numar % 2 == 0 or numar % 3 == 0:
        return False

    i = 5
    while i * i <= numar:
        if numar % i == 0 or numar % (i + 2) == 0:
            return False
        i += 6

    return True

numar = int(input("Introduceți un număr întreg: "))
if este_numar_prim(numar):
    print(f"{numar} este un număr prim.")
else:
    print(f"{numar} nu este un număr prim.")


#7.Scrieți un program care să determine ziua săptămânii pe baza unui număr de la 1 la 7, unde 1 reprezintă luni și 7 reprezintă duminică
def ziua_saptamanii(numar):
    if numar == 1:
        return "Luni"
    elif numar == 2:
        return "Marți"
    elif numar == 3:
        return "Miercuri"
    elif numar == 4:
        return "Joi"
    elif numar == 5:
        return "Vineri"
    elif numar == 6:
        return "Sâmbătă"
    elif numar == 7:
        return "Duminică"
    else:
        return "Numărul nu corespunde unei zile a săptămânii."

numar = int(input("Introduceți un număr de la 1 la 7: "))
rezultat = ziua_saptamanii(numar)
print(f"Ziua corespunzătoare numărului {numar} este {rezultat}.")

#8.Determinați dacă un număr dat este un număr par sau impar
def este_numar_par_impar(numar):
    if numar % 2 == 0:
        return "Numărul este par."
    else:
        return "Numărul este impar."

numar = int(input("Introduceți un număr întreg: "))
rezultat = este_numar_par_impar(numar)
print(rezultat)

#9.Scrieți un program care să determine dacă un an citit de la tastatură este un an bisect
def este_an_bisect(an):
    if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
        return "Anul este bisect."
    else:
        return "Anul nu este bisect."

an = int(input("Introduceți un an: "))
rezultat = este_an_bisect(an)
print(rezultat)

#10.Calculați suma a două numere întregi citite de la tastatură și afișați rezultatul
def suma_doua_numere():
    numar1 = int(input("Introduceți primul număr întreg: "))
    numar2 = int(input("Introduceți al doilea număr întreg: "))
    suma = numar1 + numar2
    print(f"Suma numerelor {numar1} și {numar2} este: {suma}")

suma_doua_numere()


#11.Determinați dacă un număr întreg citit de la tastatură este pozitiv sau negativ și afișați rezultatul
def determina_semnele_numerelor():
    numar = int(input("Introduceți un număr întreg: "))
    if numar > 0:
        print(f"Numărul {numar} este pozitiv.")
    elif numar < 0:
        print(f"Numărul {numar} este negativ.")
    else:
        print(f"Numărul {numar} este zero.")

determina_semnele_numerelor()

#12.Scrieți un program care să afișeze numerele Fibonacci până la un anumit termen citit de la tastatură și să le afișeze
def fibonacci(termen_maxim):
    a, b = 0, 1
    termen_actual = 0

    while termen_actual < termen_maxim:
        print(a, end=" ")
        a, b = b, a + b
        termen_actual += 1

termen_maxim = int(input("Introduceți termenul maxim pentru secvența Fibonacci: "))
print("Secvența Fibonacci până la termenul", termen_maxim, "este:")
fibonacci(termen_maxim)


#13.Scrieți un program care să determine suma și media a unei liste de numere citite de la tastatură
def suma_si_media_listei():
    numere = []

    n = int(input("Introduceți câte numere doriți să adăugați în listă: "))

    for i in range(n):
        numar = float(input(f"Introduceți numărul {i + 1}: "))
        numere.append(numar)

    suma = sum(numere)
    media = suma / n

    return suma, media

suma, media = suma_si_media_listei()

print(f"Suma numerelor este: {suma}")
print(f"Media numerelor este: {media:.2f}")


#15.Sortați un vector de 8 elemente citite de la tastatură, folosiți metoda Bubble Sort.
def bubble_sort(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

vector = []

print("Introduceți cele 8 elemente ale vectorului:")
for i in range(8):
    element = int(input(f"Elementul {i + 1}: "))
    vector.append(element)

bubble_sort(vector)

print("Vectorul sortat folosind Bubble Sort:")
print(vector)


#16.A se rezolva ecuația de Gradul al doilea folosind un program scris in Python
def rezolva_ecuatia_de_gradul_2(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Două rădăcini reale:", x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return "O singură rădăcină reală:", x
    else:
        parte_reală = -b / (2*a)
        parte_imaginară = math.sqrt(-discriminant) / (2*a)
        return "Două rădăcini complexe:", complex(parte_reală, parte_imaginară), complex(parte_reală, -parte_imaginară)

a = float(input("Introduceți coeficientul a: "))
b = float(input("Introduceți coeficientul b: "))
c = float(input("Introduceți coeficientul c: "))

rezultat = rezolva_ecuatia_de_gradul_2(a, b, c)
print(rezultat)

#17.Se citesc 3 numere de la tastatură să se afișeze dacă acestea pot reprezenta unghiurile unui triunghi.
def pot_forma_triunghi(a, b, c):
    if a + b + c == 180:
        return "Cele trei unghiuri pot forma un triunghi."
    else:
        return "Cele trei unghiuri nu pot forma un triunghi."
unghi1 = int(input("Introduceți primul unghi: "))
unghi2 = int(input("Introduceți al doilea unghi: "))
unghi3 = int(input("Introduceți al treilea unghi: "))

rezultat = pot_forma_triunghi(unghi1, unghi2, unghi3)
print(rezultat)
