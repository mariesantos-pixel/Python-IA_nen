import random

número_secreto= random.randint(1,100)
palpite=int(input("adivinhe um número de 1,100(apenas uma chance)"))

if palpite==número_secreto:
   print("Você acertou! ")
else:
   print(f"ERROU! O número era {número_secreto}")