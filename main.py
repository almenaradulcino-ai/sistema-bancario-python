from usuarios import criar_usuario, login
from operacoes import depositar, sacar, ver_saldo, ver_historico

usuario_logado = None

while True:

    # ==============================
    # 🔐 MENU - USUÁRIO DESLOGADO
    # ==============================
    if not usuario_logado:
        print("\n" + "="*30)
        print("   SISTEMA BANCÁRIO")
        print("="*30)
        print("1 - Criar conta")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_usuario()

        elif opcao == "2":
            usuario_logado = login()

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

    # ==============================
    # 💰 MENU - USUÁRIO LOGADO
    # ==============================
    else:
        print("\n" + "="*30)
        print(f"Usuário logado: {usuario_logado}")
        print("="*30)
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Ver histórico")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            depositar(usuario_logado)

        elif opcao == "2":
            sacar(usuario_logado)

        elif opcao == "3":
            ver_saldo(usuario_logado)

        elif opcao == "4":
            ver_historico(usuario_logado)

        elif opcao == "5":
            print("Logout realizado!")
            usuario_logado = None

        else:
            print("Opção inválida!")