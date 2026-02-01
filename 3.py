def aprovar_emprestimo():
    print("--- Simulador de Empréstimo Bancário ---")

    try:
        valor_casa = float(input("Digite o valor da casa (R$): "))
        salario = float(input("Digite o salário do comprador (R$): "))
        anos = int(input("Em quantos anos você pretende pagar? "))
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
        return

    meses = anos * 12
    prestacao_mensal = valor_casa / meses

    limite_salario = salario * 0.30

    print(f"\nValor da prestação mensal: R${prestacao_mensal:.2f}")
    print(f"Limite de 30% do salário: R${limite_salario:.2f}")

    if prestacao_mensal <= limite_salario:
        print("\nStatus: \033[92mAPROVADO\033[0m")
        print("Parabéns! Seu empréstimo foi aprovado.")
    else:
        print("\nStatus: \033[91mNEGADO\033[0m")
        print("Infelizmente, a prestação excede 30% do seu salário.")


if __name__ == "__main__":
    aprovar_emprestimo()