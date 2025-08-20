import os
import random
import time

class banco_caixa:
    dic = {}
    def __init__(self, senha, dono):
        self.numero = random.randint(1, 100000000)
        self._senha = senha
        self.dono = dono

    def criar(self):
        if not os.path.isfile(f"conta{self.numero}.txt"):
            print(f"Olá {self.dono}, sua conta é a de número {self.numero}, ela foi criada e está disponível para saques e depósitos!")
            with open(f"conta{self.numero}.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("0")
        banco_caixa.dic[self.dono] = f"conta {self.numero}"

    def excluir(self):
        if os.path.isfile(f"conta{self.numero}.txt"):
            while True:
                print("Para excluir a sua conta permanentemente digite sua senha de 3 digitos: ")
                x = input("")
                if x == self._senha:
                    os.remove(f"conta{self.numero}.txt")
                    if self.dono in banco_caixa.dic:
                        del banco_caixa.dic[self.dono]
                    print("Conta excluída")
                    break
                else:
                    print("Senha incorreta")
                    break
        else:
            print("Você não possui conta para excluir.")

    def deposito(self):
        x = float(input("Digite o valor que você deseja depositar: R$"))
        with open(f"conta{self.numero}.txt", "r", encoding="utf-8") as arquivo:
            saldo = float(arquivo.read())
            resultado = saldo + x
        with open(f"conta{self.numero}.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(str(resultado))
        print(f"{x} depositado na conta {self.numero}")

    def saque(self):
        with open(f"conta{self.numero}.txt", "r", encoding="utf-8") as arquivo:
            saldo = float(arquivo.read())
            if saldo > 0:
                x = float(input("Digite o valor que você deseja sacar: R$"))
                if x < saldo:
                    valor = saldo - x
                    with open(f"conta{self.numero}.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.write(str(valor))
                else:
                    print("Você está tentando sacar mais dinheiro do que possui na sua conta.")
            else:
                print("Você não possui dinheiro em sua conta")


nomes = ["Crislany", "Joana", "Rafaella", "Davi", "Marcos", "Pedro", "Arthur", "Laura", "Alicya"]
sobrenomes = ["Bento", "Clemente", "Honório", "Melo", "Machado", "Soares", "Costa", "Azevedo"]
SENHA_UNICA = "123"  

while True:  
    print("FILA PARA ATENDIMENTO LIVRE - APENAS UM USUÁRIO POR VEZ")
    
    pessoas = []
    for i in range(1): 
        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)
        dono = f"{nome} {sobrenome}"
        
        pessoa = banco_caixa(SENHA_UNICA, dono)  
        pessoa.criar()
        pessoas.append(pessoa)
        print(f" {dono} criou conta {pessoa.numero}")
    
    print(f"\n ATENDIMENTO: ")
    for pessoa in pessoas:
        print(f"\n {pessoa.dono} (Conta: {pessoa.numero}) ")
        
        if input("Deseja fazer depósito? (sim/não): ").lower().strip() == 'sim':
            pessoa.deposito()
        
        if input("Deseja fazer saque? (sim/não): ").lower().strip() == 'sim':
            pessoa.saque()
        
        if input("Deseja excluir conta? (sim/não): ").lower().strip() == 'sim':
            pessoa.excluir()
    
    time.sleep(2)
    os.system('cls')
    
    print("LISTA COMPLETA DE USUÁRIOS")
    for proprietario, numero_conta in banco_caixa.dic.items():
        print(f" {proprietario} -  {numero_conta}")
    print(f"\n Total acumulado: {len(banco_caixa.dic)} usuários")
   
    
    continuar = input("\nO caixa está livre, deseja ser o próximo? (sim/não): ")
    if continuar.lower().strip() != 'sim':
        print("Encerrando sistema...")
        break
    
    time.sleep(2)
    os.system('cls')