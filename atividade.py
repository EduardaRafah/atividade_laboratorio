import os

class banco_caixa:
    def __init__(self,senha,numero):
        self._senha=senha
        self.numero=numero

    def criar(self):
         if not os.path.isfile("conta.txt"):
          print(f"olá conta de número {self.numero}, você acabou acessar sua conta.")
          with open("conta.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("0")
        
    def excluir(self):
        if os.path.isfile("conta.txt"):
         while True:
          print("para excluir sua conta digite sua senha novamente.")
          x= input("")
          if x ==self._senha:
             os.remove("conta.txt")
             print("Conta excluída")
             break
          else:
             print("senha errada")
             break
        else:
           print("você não tem conta para excluir.")
    def deposito(self):
       
       x= float(input("Digite o valor que vocÊ deseja depositar."))
       with open("conta.txt", "r", encoding="utf-8") as arquivo:
           saldo = float(arquivo.read())
           resultado= saldo+x
       with open("conta.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(str(resultado))
       print(f"{x} depositado na conta {self.numero}")

    def saque(self):
        
         with open("conta.txt", "r", encoding="utf-8") as arquivo:
           saldo = float(arquivo.read())
           if saldo>0:
            x= float(input("Digite o valor que vocÊ deseja sacar."))
            if x<saldo:
             valor= saldo-x
             with open("conta.txt", "w", encoding="utf-8") as arquivo:
              arquivo.write(str(valor))
            else:
               print("Você está tentando sacar mais do que tem.")
           else:
              print("Você não tem dinheiro na conta")
      
pessoa = banco_caixa("123" , 23)
pessoa.criar()
pessoa.deposito()
pessoa.saque()
    
    