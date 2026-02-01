# Coleta de dados do usuário
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado com 2 casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Classificação segundo a OMS
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

