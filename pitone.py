#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[3]:


numero1=int(input("inserisci il primo numero: "))
numero2=int(input("inserisci il secondo numero: "))
moltiplicazione=numero1*numero2
print("la moltiplicazione è:", moltiplicazione)


# In[8]:


for numero in range(1,11):
    print(numero)


# In[9]:


for numero in range(1,10+1):
    print(numero)


# In[4]:


operazione=input("inserisci l'operazione (+, -, *, /): ")

numero1=float(input("inserisci il primo numero: "))
numero2=float(input("inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1+numero2
elif operazione == "-":
    risultato = numero1-numero2
elif operazione == "*":
    risultato = numero1*numero2
elif operazione == "/":
    risultato = numero1/numero2
else:
    risultato = "operazione non valida"
    
print("il risultato è: ", risultato)


# In[14]:


n=int(input("inserisci un numero intero positivo:"))

for numero in range(5,n+1):
    print(numero)


# In[21]:


n=int(input("inserisci un numero intero positivo:"))
somma=0

for numero in range(1,n+1):
    #somma + numero=
    somma += numero
    #se in "for numero in range" ripeterà il comando su tutti i numeri
print("la somma dei primi", n, "numeri interi è:", somma)


# In[22]:


n=int(input("inserisci un numero intero positivo: "))

print("quadrati dei primi:", n, "numeri:")

for numero in range(1,n+1):
    quadrato=numero ** 2
    print("il quadrato di", numero, "è", quadrato)


# In[13]:


numero=int(input("inserisci un numero: "))

if numero % 2 == 0:
    #se ""% 10 == 3:" sono pari solo i numeri che divisi per 10 danno come resto 3"
    print(numero, "è un numero pari.")
else:
    print(numero, "è un numero dispari.")


# In[5]:





# In[6]:





# In[9]:





# In[1]:





# n=int(input("iserisci un numero intero positivo: "))
# fattoriale=1
# 
# for numero in range(1, n+1):
#     fattoriale*=numero
# print("il fattoriale di", n, "è:", fattoriale)

# In[27]:


numeri=[]

n=int(input("quanti numeri vuoi inserire? "))

for i in range(n):
    numero=float(input("inserisci un numero: "))
    numeri.append(numero)
    
media=sum(numeri)/len(numeri)

print("la media dei numeri inseriti è:", media, "la lista completa è:", numeri)


# In[28]:


import random

numero_da_indovinare=random.randint(1, 100)
tentativi=0

while True:
    tentativo=int(input("indovina il numero (1-100): "))
    tentativi+=1
    
    if tentativo==numero_da_indovinare:
        print("Bravo! Hai indovinato il numero", numero_da_indovinare, "in", tentativi, "tentativi.")
        break
    elif tentativo<numero_da_indovinare:
        print("il numero da indovinare è più grande.")
    else:
        print("il numero da indovinare è più piccolo.")


# In[ ]:





# In[5]:


n=int(input("inserisci numero: "))

fattoriale=1

if n<0:
    print("aspetta... solo numeri positivi")
elif n==0:
    print("deve essere intero")
else:
    for numero in range(1,1+n):
        fattoriale*=numero
print(f"il numero fattoriale di {n} è {fattoriale}")


# In[ ]:





# In[8]:


frase=input("inserisci una frase ").lower()
CV=0
V="aeiou"
for carattere in frase:
    if carattere in V:
        CV+=1
#la "f" prima delle "" serve a renderle più flessibili per inserire variabili come CV
print(f"nella frase ci sono {CV} vocali")


# In[ ]:





# In[5]:





# In[ ]:





# In[4]:


popolazione=int(input("inserisci la popolazione iniziale: "))
anni=int(input("inserisci numero di anni da simulare: "))
tasso_natalità=float(input("inserisci il tasso di natalità: "))
tasso_mortalità=float(input("inserisci il tasso di mortalità"))

for anno in range(anni):
    nascite=(popolazione*tasso_natalità)/100
    morti=(popolazione*tasso_mortalità)/100
    popolazione+=(nascite-morti)
    
    print(f"Anno {anno+1}: Popolazione= {int(popolazione)}")

    print("Simulazione completata.")


# In[ ]:





# In[5]:


import datetime

today=datetime.datetime.today()
print(f"oggi è il giorno: {today:%d / %m / %Y} ore: {today:%H : %M : %S}")


# In[2]:


print("Benvenuto nel Convertitore di Unità di Misura!")

scelta=input("cosa vuoi convertire (metri/piedi, libbre/chilogrammi)")

if scelta=="metri":
    valore=float(input("inserisci il valore in metri: "))
    risultato=valore*3.28084
    print(f"{valore} metri corrispondono a {risultato} piedi")
    
elif scelta=="piedi":
    valore=float(input("inserisci il valore in piedi: "))
    risultato=valore/3.28084
    print(f"{valore} piedi corrispondono a {risultato} metri")
    
elif scelta=="chilogrammi":
    valore=float(input("inserisci il valore in chilogrammi: "))
    risultato=valore*2.20462
    print(f"{valore} chilogrammi corrispondono a {risultato} libbre")

elif scelta=="libbre":
    valore=float(input("inserisci il valore in libbre: "))
    risultato=valore*2.20462
    print(f"{valore} libbre corrispondono a {risultato} chilogrammi")

else:
    print("scelta non valida. scegli tra 'metri'/'piedi', 'chilogrammi'/'libbre'")


# In[ ]:





# In[4]:


n=int(input("inserisci un numero n per calcolare l'n-esimo numero di Fibonacci: "))

a=0
b=1
c=a+b

if n<=0:
    print("il numero deve essere maggiore di 0.")
    
elif n==1:
    risultato=a
else:
    for interazione in range(n-3):
        a=b
        b=c
        c=a+b
    risultato=c
    
print("l'n-esimo numero di Fibonacci è:", risultato)


# In[ ]:





# In[3]:


#def=definisci
def fibonacci(n):
    fib_series=[0,1]
    
    while len(fib_series)<n:
        fib_series.append(fib_series[-1]+fib_series[-2])
        
    return fib_series


# In[4]:


fibonacci(12)


# In[ ]:





# In[5]:


n=int(input("inserisci il numero di termini della serie di fibonaccida generare: "))

if n<=0:
    print("inserisci un numero positivo.")
else:
    result=fibonacci(n)#result=output(riceve input e output)
    print(result)


# In[ ]:





# In[4]:


import math

def calcola_area_cerchio(raggio):
    return math.pi*(raggio**2)

def calcola_area_rettangolo(base, altezza):
    return base*altezza

def calcola_area_trangolo(base, altezza):
    return (base*altezza)/2


# In[7]:


calcola_area_cerchio(10)


# In[12]:


print("benvenuto nella calcolatrice di aree")


scelta=input("vuoi calcolare l'area di un cerchio (c), rettangolo (r), triangolo (t)? ")

if scelta =='c':
    raggio=float(input("inserisci il raggio del cerchio: "))
    area=calcola_area_cerchio(raggio)
    print(f"l'area del cerchio è {area: .2f}")

elif scelta=='r':
    base=float(input("inserisci la base del rettangolo: "))
    altezza=float(input("inserisci l'altezza del rettangolo: "))
    area=calcola_area_rettangolo(base, altezza)
    print(f"l'area del rettangolo è {area: .2f}")

elif scelta=='t':
    raggio=float(input("inserisci la base del triangolo: "))
    raggio=float(input("inserisci l'altezza del triangolo: "))
    area=calcola_area_rettangolo(base, altezza)
    print(f"l'area del triangolo è {area: .2f}")
else:
    print("puoi inserire solo c, r, t")


# In[1]:


def calcola_interessi(importo_iniziale, tasso_interesse, periodo_investimento):
    importo_finale=importo_iniziale*(1+tasso_interesse/100)**periodo_investimento
    return importo_finale


# In[2]:


print("benvenuto nel calcolatore di interessi! ")

importo=float(input("inserisci l'importo iniziale: "))
tasso=float(input("inserisci il tasso di interesse annuale(%): "))
periodo=float(input("inserisci il periodo di investimento (anni): "))

importo_finale= calcola_interessi(importo, tasso, periodo)
print(f"l'importo finale è {importo_finale: .2f}")


# In[ ]:





# In[6]:


def forza_gravitazionale(m1, m2, r):
    # Costante gravitazionale
    G=6.67430e-11 # N(m/kg)^2
    
    # Calcolo della forza gravitazionale
    F=(G*m1*m2)/(r**2)
    
    return F


# In[9]:


#esempio di utilizzo
Massa_Terra=5.972e24 #kg
Massa_Luna=7.342e22
Distanza_Terra_Luna=384400000

forza=forza_gravitazionale(Massa_Terra, Massa_Luna, Distanza_Terra_Luna)
print(f"Forza Gravitazionale tra la Terra e la Luna: {forza} Newton")


# In[3]:





# In[4]:


from itertools import permutations
k=0

def trova_anagrammi(parola):
    anagrammi=["".join(p) for p in permutation(parola)]
    return anagrammi


# In[6]:


from itertools import permutations

def trova_anagrammi(parola):
    return set([''.join(p) for p in permutations(parola)])

print("Benvenuto nel Risolutore di Anagrammi!")

parola_input = input("Inserisci una parola: ").strip().lower()  # strip spazi bianchi lower in minuscolo

if len(parola_input) < 2:
    print("Inserisci una parola con almeno 2 caratteri.")
else:
    anagrammi = trova_anagrammi(parola_input)
    k = 0 

    for elemento in anagrammi:
        if elemento != parola_input:
            k += 1
            print(elemento)

    print(f"Gli anagrammi unici di '{parola_input}' sono in totale: {k}")


# In[8]:


#definizione dei tassi di cambio

tassi_di_cambio={
    "dollari": 1.0,
    "euro": 0.85,
    "yen": 110.41,
    #aggiungi altre valute e tassi di cambio se necessario
}

#chiedi all'utente di inserire l'importo, la valuta di partenza e la valuta di destinazione
importo=float(input("inserisci l'importo da convertire: "))
valuta_di_partenza=input("inserisci la valuta di partenza: ").lower()
valuta_di_destinazione=input("inserisci la valuta di destinazione: ").lower()

#verifica se le valute sono nel dizionario dei tassi di cambio
if valuta_di_partenza in tassi_di_cambio and valuta_di_destinazione in tassi_di_cambio:
    #calcola il tasso di cambio e l'importo invertito
    tasso_di_cambio=tassi_di_cambio[valuta_di_destinazione]/tassi_di_cambio[valuta_di_partenza]
    importo_convertito=importo*tasso_di_cambio
    
    #stampa il risultato
    print(f"{importo} {valuta_di_partenza} sono equivalenti a {importo_convertito: .2f} {valuta_di_destinazione}")
else:
    print("valute non supportate. assicurati di inserire valute valide.")


# In[ ]:





# In[4]:


frase=input("inserisci una frase: ")

frase=frase.lower()

alfabeto= 'abcdefghijklmnopqrstuvwxyz'

conteggio_lettere={}

for lettera in alfabeto:
    conteggio=frase.count(lettera)
    
if conteggio>0:
    conteggio_lettere[lettera]=conteggio


# In[ ]:





# In[ ]:




