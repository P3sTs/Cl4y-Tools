#!/usr/bin/env python3
import random 
# Criador do Gerador #Cl4y#
from time import sleep
opcao = 0


list1 = [50, 60, 636368, 636369, 438935, 504175, 451416, 636297, 5067, 4576, 4011, 506699,]
list = [ 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2035, 2036, 2037, 2038, 2049, 2050,]
list3 = ("abacate", "uva", "maça",)


binlist1 = random.choice(list1)	
cvv = random.randint(3, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99999999999)
senha3 = random.choice(list3)	



print("[ 1 ] CPF.")

print("[ 2 ] Gerar CCFUL.")

print("[ 3 ] Bin Válida.")

print("[ 4 ] Sair do Programa.")
 
opcao = int(input("Qual foi a sua Escolha:-->"))

if opcao == 1:
    	print("CPF", cpf)
	
if opcao == 2:
    nume2 = random.randrange(1, 9999999999999999)
    print("Número do cartão", bin,nume2)
    print("Cvv do cartão:",cvv)
    print("Data do cartão:", data1, data2, data3)
    print("CPF cadastrado no cartão:", cpf)

if opcao == 3:
	print("Bin-Valida:",binlist1)
	
if opcao == 4:

	print("Finalizado Script ")
	exit()
	print("=-=" * 10)
print("Fim do Programa! Volte Sempre!!")	
