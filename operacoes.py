import json


def carregar_dados():
    try:
        with open("dados.json", "r") as f:
            return json.load(f)
    except:
        return {}


def salvar_dados(dados):
    with open("dados.json", "w") as f:
        json.dump(dados, f, indent=4)


def depositar(usuario):
    dados = carregar_dados()

    try:
        valor = float(input("Valor do depósito: "))
    except:
        print("Valor inválido!")
        return

    if valor <= 0:
        print("Valor inválido!")
        return

    dados[usuario]["saldo"] += valor

    # histórico
    dados[usuario]["historico"].append(f"Depósito: +R$ {valor:.2f}")

    salvar_dados(dados)
    print("Depósito realizado com sucesso!")


def sacar(usuario):
    dados = carregar_dados()

    try:
        valor = float(input("Valor do saque: "))
    except:
        print("Valor inválido!")
        return

    if valor <= 0:
        print("Valor inválido!")
        return

    if dados[usuario]["saldo"] >= valor:
        dados[usuario]["saldo"] -= valor
        dados[usuario]["historico"].append(f"Saque: -R$ {valor:.2f}")
        print("Saque realizado!")
    else:
        print("Saldo insuficiente!")

    salvar_dados(dados)


def ver_saldo(usuario):
    dados = carregar_dados()
    saldo = dados[usuario]["saldo"]
    print(f"Saldo atual: R$ {saldo:.2f}")


def ver_historico(usuario):
    dados = carregar_dados()

    print("\n📊 Histórico de transações:")

    historico = dados[usuario].get("historico", [])

    if not historico:
        print("Nenhuma transação encontrada.")
    else:
        for item in historico:
            print("-", item)