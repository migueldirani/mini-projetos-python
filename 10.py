primeira_nota = float(input('Qual sua primeira nota? '))
segunda_nota = float(input('Qual é sua segunda nota? '))
media = primeira_nota + segunda_nota /2


if media <5:
    print('reprovado')
elif media <5 and 6.9:
    print('recuperação ')
elif media > 7:
    print('aprovado')

