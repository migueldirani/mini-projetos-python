# Função para mostrar a tabuada
def mostrar_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1,11):  # Vai de 1 até onde setar o segundo numero
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Função principal
def main():
    # Entrada do número
    numero = int(input("Digite um número para ver sua tabuada: "))
    mostrar_tabuada(numero)

# Chamando a função principal
if __name__ == "__main__":
    main()
