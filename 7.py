peso = float(input('Qual seu peso atual? '))
altura = float(input('Qual é sua altura atual? '))

imc = peso/ (altura**2)
print(f'Seu IMC é: {imc:.2f}')


if imc <18.5:
    print('Abaixo do peso ideal')
elif 18.5  <= imc <25:
    print('Peso ideal')
elif imc <25 <= imc < 30:
    print('Sobrepeso')
elif imc <30  <= imc <40:
    print('Obesidade ')
else:
    print('Obesidade morbida')
