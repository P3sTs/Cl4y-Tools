#!/usr/bin/env python3
import os
import random 
# Criador do Gerador #Cl4y#
from time import sleep
opcao = 0


# lista de bin
list1 = [ 35, 38, 60, 50, 60, 636368, 636369, 438935, 504175, 451416, 636297, 5067, 4576, 4011, 506699,]
# lista data de vencimento
list = [ 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2035, 2036, 2037, 2038, 2049, 2050,]
# Lista de senhas
list3 =("ivyjovan",
"mividaes1kk",
"mividaes10",
"mividaerstuteamo",
"mividaenrosa","mividaelrock@hotmail.com",
"mividaelparaiso","mividaeamo","mividadura",
"mividadiva","mividadios",
"mividadieguis","ividadetrasdelatuya",
"mividaderstu",
"mividadeamor","mividadary","mividadali","mividacontinua","mividaconel","mividacondios","mividaconderek-2","Pedro171", "Yuri157", "Igor69", "Matheus666", "Francisco1234", "José123", "João232", "Carlos1341", "Paulo222", "Lucas420", "Marcelo45", "Daniel155", "Raimundo1", "Rodrigo123", "Eduardo445", "Luiz" "Diego", "Kaike"
)
#lista de nomes
name = ("Pedro", "Yuri", "Igor", "Matheus", "Francisco", "José", "João", "Carlos", "Paulo", "Lucas", "Marcelo", "Daniel", "Raimundo", "Rodrigo", "Eduardo", "Luiz" "Diego", "Kaike") 

name2 = ("Pereira", "Silva", "Roberto", "Carneiro",)
 
name3 = ("Henrique", "Grabriel",  "Dantas", "Silva", "David",) 

nume2 = random.randrange(1, 9999999999)
binlist1 = random.choice(list1)	
cvv = random.randint(3, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99999999999)
senha3 = random.choice(list3)	
listname = random.choice(name)
listname2 =  random.choice(name2)
listname3 =  random.choice(name3)
listname4 =  random.choice(name3)


print ("[ 1 ] CPF.                                                                                                              ")

print ("[ 2 ] Gerar CCFUL.                                                                                                      ")

print ("[ 3 ] Bin Válida.                                                                                                       ")

print ("[ 4 ] Gerar Senha E CPF.                                                                                                ")

print ("[ 5 ] CVV.                                                                                                              ")

print ("[ 6 } Gerar Nome.                                                                                                       ")

print ("[ 0 ] Sair do Programa.                                                                                                 ")

 
opcao = int(input("Qual foi a sua Escolha:-->"))



if opcao == 1:

    	print("CPF:-->", cpf)
	
if opcao == 2:
    print("Nome do Cadastrado:-->", listname, listname2, listname3, listname4 )
    
    print("Número do cartão:-->", binlist1,nume2)

    print("Cvv do cartão:-->",cvv)

    print("Data do cartão:-->", data1, data2, data3)

    print("CPF cadastrado no cartão:-->", cpf)


if opcao == 3:
	print("Bin-Valida:--> ",binlist1)
if opcao == 4:
	print ("CPF:--> ", cpf)

	print ("SENHA:--> ", senha3)
	
if opcao == 5:
	print ("CVV:--> ", cvv)

if opcao == 6:
	print ("CPF:-->", cpf)
	
	print ("Nome:-->", listname, listname2, listname3, listname4)
	
if opcao == 0:

	print("Finalizado Script ")

	exit()

	print("=-=" * 10)
print("Fim do Programa! Volte Sempre!!")	
