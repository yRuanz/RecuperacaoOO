from Classes import *
import os

def main():

    banco = {}

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("--- MENU DO BANCO ---\n")
            print("1 - CRIAR CONTA")
            print("2 - SACAR")
            print("3 - DEPOSITAR")
            print("4 - TRANSFERIR")
            print("5 - SALDO")
            print("0 - SAIR")
            print("----------------------\n")

            print("Qual opção deseja?")
            menu = int(input(">>"))
            os.system("pause")
            os.system("cls")

            match menu:
                case 1:
                    print("--- CRIAR CONTA ---")
                    nome = input("Coloque seu nome: ")
                    saldo_inicial = int(input("Saldo inicial:R$ "))

                    if nome and saldo_inicial == True:
                        print("CADASTRO COMPLETO!")
                        print(f"SEJA BEM VINDO(A) {nome}") 
                    os.system("pause")
                    os.system("cls")
                case 2:
                    print("--- SACAR ---")
                    conta = input("Coloque sua conta: ")
                    valor = int(input("Quanto deseja sacar? "))

                    if valor <= saldo_inicial:
                        saldo_inicial = self.saldo_inicial - self.valor
                        print(" --- SAQUE BEM SUCEDIDO! ---")
                        print(f"VOCÊ SACOU R${valor} !")
                    else:
                        valor > saldo_inicial
                        print("SAQUE INTERROMPIDO!")
                    os.system("pause")
                    os.system("cls")
                case 3:
                    print("--- DEPOSITAR ---")
                    conta = input("Coloque sua conta: ")
                    valor = int(input("Quanto deseja depositar? "))

                    if self.valor > 0:
                        saldo_inicial = self.saldo_inicial + self.valor
                        print(" --- DEPOSITO BEM SUCEDIDO! ---")
                        print(f"VOCÊ DEPOSITOU R${valor} !")
                    else:
                        print("DEPOSITO INTERROMPIDO!")
                    os.system("pause")      
                    os.system("cls")
                case 4:
                    print("--- TRANSFERIR ---")
                    origem = print(nome)
                    destino = input("Coloque o nome do usuário(destinátario): ")
                    valor = int(input("Coloque o valor que deseja transferir: R$"))

                    if destino in banco == True:
                        origem.saldo_inicial - valor
                        destino.saldo_inicial + valor

                        print(" TRANSFERÊNCIA COMPLETA! ")
                        print(f"{origem} transferiu R${valor} para {destino}.")
                    os.system("pause")
                    os.system("cls")
                case 5:
                    print("--- SALDO ---")
                    print(f"Nome:{self.nome} - Saldo:{saldo_inicial}")
                    os.system('pause')      
                    os.system("cls")  
                case 0:
                    print("SAINDO...")
                    sair = True

                case _:
                    print("- !! VALOR INVÁLIDO !! -")

        except Exception as erro:
            print(erro.__class__.__name__)
            print(" ")