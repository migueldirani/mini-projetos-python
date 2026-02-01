primeira_nota = float(input('Qual sua primeira nota? '))
segunda_nota = float(input('Qual é sua segunda nota? '))
media = (primeira_nota + segunda_nota) / 2  # precisa dos parênteses

if media < 5:
    print('Reprovado')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Aprovado')
