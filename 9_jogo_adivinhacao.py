import random
numero = random.randint(1, 10)
chute = int(input("Tente adivinhar o número entre 1 e 10: "))
if chute == numero:
    print("Parabéns! Você acertou!")
else:
    print(f"Errado! O número era {numero}")
