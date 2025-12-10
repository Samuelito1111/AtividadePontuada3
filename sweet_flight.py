# Samuel Sousa Oliveira da Cruz
# Natália Costa da Silva 

import os
import time
from dataclasses import dataclass

@dataclass
class Reserva:
    numero_aviao: str
    nome_passageiro: str

vetor_avioes = [None] * 4
vetor_assentos = [0] * 4

lista_reservas = []
MAX_RESERVAS = 20

def limpar_tela():
    os.system("cls || clear")

def pausar():
    input("\nPressione Enter para continuar...")

def registrar_avioes():
    print("\n1. Registrar Numeros dos Avioes")
    for i in range(4):
        vetor_avioes[i] = input(f"Digite o numero do aviao {i+1}: ")
    print("Avioes cadastrados com sucesso!")

def registrar_assentos():
    print("\n2. Registrar Assentos Disponiveis")
    
    if vetor_avioes[0] is None:
        print("Erro: Cadastre os avioes na Opcao 1 primeiro!")
        return

    for i in range(4):
        print(f"Aviao: {vetor_avioes[i]}")
        try:
            qtd = int(input(" -> Quantos assentos disponiveis? "))
            vetor_assentos[i] = qtd
        except ValueError:
            print("Erro: Digite apenas numeros inteiros.")
            vetor_assentos[i] = 0

    print("Assentos cadastrados com sucesso!")

def realizar_reserva():
    print("\n3. Reservar Passagem Aerea")

    if len(lista_reservas) >= MAX_RESERVAS:
        print("Limite de reservas atingido (20 reservas)!")
        return

    if vetor_avioes[0] is None:
        print("Erro: Nao ha avioes cadastrados.")
        return

    aviao_busca = input("Digite o numero do aviao: ")
    
    indice_encontrado = -1
    for i in range(4):
        if vetor_avioes[i] == aviao_busca:
            indice_encontrado = i
            break
    
    if indice_encontrado == -1:
        print("Este aviao nao existe!")
        return

    assentos_disponiveis = vetor_assentos[indice_encontrado]
    
    if assentos_disponiveis > 0:
        nome = input("Digite o nome do passageiro: ")
        
        nova_reserva = Reserva(numero_aviao=aviao_busca, nome_passageiro=nome)
        lista_reservas.append(nova_reserva)
        
        vetor_assentos[indice_encontrado] -= 1
        
        print("Reserva realizada com sucesso!")
    else:
        print("Nao ha assentos disponiveis para este aviao!")

def consultar_por_aviao():
    print("\n4. Consultar por Aviao")
    aviao_busca = input("Digite o numero do aviao: ")

    if aviao_busca not in vetor_avioes:
        print("Este aviao nao existe!")
        return

    print(f"--- Lista de passageiros do aviao {aviao_busca} ---")
    encontrou_reserva = False
    
    for reserva in lista_reservas:
        if reserva.numero_aviao == aviao_busca:
            print(f"- {reserva.nome_passageiro}")
            encontrou_reserva = True
    
    if not encontrou_reserva:
        print("Nao ha reservas realizadas para este aviao!")

def consultar_por_passageiro():
    print("\n5. Consultar por Passageiro")
    nome_busca = input("Digite o nome do passageiro: ")
    
    encontrou = False
    print(f"--- Voos de {nome_busca} ---")
    
    for reserva in lista_reservas:
        if reserva.nome_passageiro.lower() == nome_busca.lower():
            print(f"- Aviao: {reserva.numero_aviao}")
            encontrou = True
            
    if not encontrou:
        print("Nao ha reservas realizadas para este passageiro!")

def main():
    while True:
        limpar_tela()
        print("SWEET FLIGHT - GESTAO DE RESERVAS")
        print(f"Total de Reservas: {len(lista_reservas)}/{MAX_RESERVAS}")
        print("-" * 30)
        print("1. Registrar Avioes")
        print("2. Registrar Assentos")
        print("3. Reservar Passagem")
        print("4. Consultar por Aviao")
        print("5. Consultar por Passageiro")
        print("6. Encerrar Sistema")
        print("-" * 30)
        
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            registrar_avioes()
            pausar()
        elif opcao == '2':
            registrar_assentos()
            pausar()
        elif opcao == '3':
            realizar_reserva()
            pausar()
        elif opcao == '4':
            consultar_por_aviao()
            pausar()
        elif opcao == '5':
            consultar_por_passageiro()
            pausar()
        elif opcao == '6':
            print("Encerrando sistema...")
            break
        else:
            print("Opcao invalida!")
            time.sleep(1)

if __name__ == "__main__":
    main()