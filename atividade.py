class Emprestimo:
    def __init__(self, valor: float, quitado: bool = False):
        self.valor = valor
        self.quitado = quitado

    def __str__(self):
        status = "Quitado" if self.quitado else "Pendente"
        return f"R$ {self.valor:.2f} ({status})"

class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        self.emprestimos.append(emprestimo)

    def verificar_aptidao(self):
        emprestimos_pendentes = [emp for emp in self.emprestimos if not emp.quitado]
        qtd_pendentes = len(emprestimos_pendentes)
        divida_total = sum(emp.valor for emp in emprestimos_pendentes)

        if qtd_pendentes >= 2:
            return False, f"Possui {qtd_pendentes} empréstimo(s) pendente(s) (Limite: 1)."
        
        if divida_total > 10000:
            return False, f"Dívida total de R$ {divida_total:.2f} ultrapassa o limite de R$ 10.000,00."

        return True, "Cliente apto para novo empréstimo."

def menu():
    banco_de_clientes = {}

    while True:
        print("\n--- SISTEMA DE EMPRÉSTIMOS ---")
        print("1 - Cadastrar Cliente")
        print("2 - Registrar Novo Empréstimo")
        print("3 - Verificar Aptidão de Cliente")
        print("4 - Listar Clientes e Situações")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            if cpf not in banco_de_clientes:
                banco_de_clientes[cpf] = Cliente(nome, cpf)
                print("✅ Cliente cadastrado com sucesso!")
            else:
                print("⚠️ CPF já cadastrado no sistema.")
        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ")
            cliente = banco_de_clientes.get(cpf)
            
            if cliente:
                apto, motivo = cliente.verificar_aptidao()
                if apto:
                    try:
                        valor = float(input("Digite o valor do empréstimo: R$ "))
                        novo_emprestimo = Emprestimo(valor)
                        cliente.adicionar_emprestimo(novo_emprestimo)
                        print("✅ Empréstimo registrado com sucesso!")
                    except ValueError:
                        print("❌ Valor inválido.")
                else:
                    print(f"❌ Empréstimo negado. Motivo: {motivo}")
            else:
                print("⚠️ Cliente não encontrado.")
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ")
            cliente = banco_de_clientes.get(cpf)
            
            if cliente:
                apto, motivo = cliente.verificar_aptidao()
                if apto:
                    print(f"✅ O cliente {cliente.nome} ESTÁ APTO. ({motivo})")
                else:
                    print(f"❌ O cliente {cliente.nome} NÃO ESTÁ APTO. ({motivo})")
            else:
                print("⚠️ Cliente não encontrado.")
        elif opcao == "4":
            if not banco_de_clientes:
                print("Nenhum cliente cadastrado.")
            for cpf, cliente in banco_de_clientes.items():
                print(f"\nCliente: {cliente.nome} | CPF: {cliente.cpf}")
                if not cliente.emprestimos:
                    print("  - Nenhum empréstimo registrado.")
                else:
                    for i, emp in enumerate(cliente.emprestimos, 1):
                        print(f"  - Empréstimo {i}: {emp}")
        elif opcao == "5":
            print("👋 Saindo do sistema de empréstimos...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
