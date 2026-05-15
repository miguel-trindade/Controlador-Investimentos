import csv

def obter_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < 0:
                print("Digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def obter_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um número inteiro positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


def exportar_csv(dados):
    nome = input("\nDigite o nome do arquivo para salvar: ")
    
    try:
        with open(f"{nome}.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Mês", "Rendimento", "Saldo"])
            writer.writerows(dados)
        print(f"Arquivo '{nome}.csv' salvo com sucesso.")
    except Exception as e:
        print("Erro ao salvar arquivo:", e)



def preco_fixo():
    print("\n--- Simulação por Tempo Fixo ---")
    
    valor_inicial = obter_float("Valor inicial: ")
    aporte = obter_float("Aporte mensal: ")
    taxa = obter_float("Taxa de juros mensal (%): ") / 100
    meses = obter_int("Quantidade de meses: ")

    saldo = valor_inicial
    historico = []

    for mes in range(1, meses + 1):
        rendimento = saldo * taxa
        saldo += rendimento + aporte
        
        historico.append([mes, round(rendimento, 2), round(saldo, 2)])
        print(f"Mês {mes}: Rendimento = {rendimento:.2f} | Saldo = {saldo:.2f}")

    exportar_csv(historico)



def calculo_meta():
    print("\n--- Cálculo de Meta Financeira ---")
    
    valor_inicial = obter_float("Valor inicial: ")
    aporte = obter_float("Aporte mensal: ")
    taxa = obter_float("Taxa de juros mensal (%): ") / 100
    meta = obter_float("Valor desejado: ")

    saldo = valor_inicial
    mes = 0
    historico = []

    while saldo < meta:
        mes += 1
        rendimento = saldo * taxa
        saldo += rendimento + aporte
        
        historico.append([mes, round(rendimento, 2), round(saldo, 2)])

    print(f"\nMeta atingida em {mes} meses.")
    print(f"Saldo final: {saldo:.2f}")

    exportar_csv(historico)



def menu():
    while True:
        print("\n=== SIMULADOR DE INVESTIMENTOS PRO ===")
        print("1. Simular por Tempo Fixo")
        print("2. Calcular Tempo para Meta")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            preco_fixo()
        elif opcao == '2':
            calculo_meta()
        elif opcao == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")




if __name__ == "__main__":
    menu()