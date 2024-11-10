"""
Reto: "El Juego de Adivina el Número"
Escribe un programa en Python en el que la computadora elija un número aleatorio entre 1 y 100,
y el usuario tenga que adivinarlo. El programa debe darle pistas al usuario, diciendo si el número que ha introducido es mayor o menor que el número secreto, hasta que lo adivine.
Instrucciones:
La computadora selecciona un número aleatorio entre 1 y 100.
El usuario introduce su suposición.
Si el número es demasiado bajo, la computadora le dice "Demasiado bajo".
Si el número es demasiado alto, la computadora le dice "Demasiado alto".
El juego continúa hasta que el usuario adivine el número correcto.
Pistas:
Usa la función random.randint() para elegir un número aleatorio.
Usa un bucle while para seguir pidiendo al usuario que adivine hasta que acierte.
"""

import random

number = random.randint(1, 100)

while True:
  guess = input("adivina el numero del 1 al 100")
  
  if guess == number:
    print("acertaste!")
    question = input("quieres intentar de nuevo? s/n")
    if question == "s":
      number = random.randint(1, 100)

    else:
      question = input("quieres intentar de nuevo? s/n")
  
  elif guess < number:
    print("el numero es mas grande que", guess)
  
  elif guess > number:
    print("el numero es mas pequeño que", guess)
