from random import *
# Ejercicio 1

# Planteo dos condiciones para casos especificos como serian el 1 y el 2, y luego verifico el modulo de el numero con todos los anteriores

def is_prime_number(number):
    if number == 2:
        print(str(number) + ' is a prime number')
        return False
    elif number == 1:
        print(str(number) + ' is not a prime number')
        return True
    for i in range(2, number):
        if number % i == 0:
            print(str(number) + ' is not a prime number')
            return False
    print(str(number) + ' is a prime number')
    return True

# Pruebas ejercicio 1
# Se podria usar la funcion de input para que verifique si es primo o no un numero que pida el usuario
is_prime_number(1)
is_prime_number(2)
is_prime_number(17)
is_prime_number(18)
is_prime_number(99)

# Ejercicio 2

# Planteo una funcion por operacion para que quede mas prolijo

def statistics_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def statistics_average(numbers, list_len):
    return float(statistics_sum(numbers)/int(list_len))

def statistics_maximun(numbers):
    max_value = 0
    for i in numbers:
        if i > max_value:
            max_value = i
    return max_value        

def statistics_minimum(numbers):
    min_value = 1000
    for i in numbers:
        if i < min_value:
            min_value = i
    return min_value  

# Imprime los resultados de cada funcion
def calculate_satistics(numbers):
    print(str(statistics_sum(numbers)) + ' <-- This is the total')
    print(str(statistics_average(numbers, list_len)) + ' <-- This is the average')
    print(str(statistics_maximun(numbers)) + ' <-- This is the maximun value')
    print(str(statistics_minimum(numbers)) + ' <-- This is the minimum value')

# Creo una lista vacia, y luego mediante un loop, le ingreso numeros random con una medida random
    
numbers_list = []
for i in range(1, randint(2, 25)):
    numbers_list.append(randint(1, 100))
list_len = len(numbers_list)
print(numbers_list)

# Prueba ejercicio 2

calculate_satistics(numbers_list)

# Ejercicio 3

def word_count(text):
    for word in text:
        if word in word_codes:
            word_codes[word] += 1
        else:
            word_codes[word] = 1
    return word_codes

short_text = 'Black screen with text; The sound of buzzing bees can be heard According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees dont care what humans think is impossible. (Barry is picking out a shirt) Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Lets shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello Barry Adam Can you believe this is happening I cant. Ill pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. Im excited. Heres the graduate. Were very proud of you, son.'
# Paso todo el texto a minuscula para que no haya complicaciones en el diccionario
short_text = short_text.lower()
# Lo paso a una lista para comprar palabras
word_list = short_text.split()
# Creo el diccionario vacio para insertar las palabras
word_codes = {}
word_codes = word_count(word_list)
ranking_word_count = {}
# Ordeno el diccionario por valor de los values de manera ascendente
word_codes = sorted(word_codes.items(), key=lambda x:x[1])
print(word_codes)

# Funcion que se itera 10 veces metiendo en un nuevo diccionario empezando por el ultimo item del diccionario anterior

def word_ranking(word_codes):
    for i in range(1, 11):
       ranking_word_count[i] = [word_codes[-i]]
    return ranking_word_count
word_ranking(word_codes)
print(ranking_word_count)
