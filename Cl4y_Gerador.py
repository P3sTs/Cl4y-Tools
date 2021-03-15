# Criador do Gerador #Cl4y#
#!/bin/bash
#!/usr/bin/env python3
import re
import requests
from subprocess import run
from os import system
import os
import random 

from time import sleep
opcao = 0
import getpass
from random import randint
# Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

clear = lambda: os.system('clear')

def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def cpf_generate():
    #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    #  Gera os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    #  Retorna o CPF como string
    result = ''.join(map(str, cpf))
    return result



list1 = [ 35, 38, 60, 50, 60, 636368, 636369, 438935, 504175, 451416, 636297, 5067, 4576, 4011, 506699,]
# lista data de vencimento
list = [ 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2035, 2036, 2037, 2038, 2049, 2050,]
# Lista de senhas
list3 =("ivyjovan",
"mividaes1kk",
"mividaes10",
"mividaerstuteamo",
"mividaerstu",
"mividaerrada",
"mividaerestusoly",
"mividaeresturkl",
"mividaeresturami",
"mividaerestur",
"mividaerestuloca",
"mividaerestujair",
"mividaerestuivon",
"mividaerestufr4n",
"mividaerestubrenda141516",
"mividaerestubb",
"mividaerestu6405",
"mividaerestu3112",
"mividaerestu3003",
"mividaerestu3",
"mividaerestu2706",
"mividaerestu24",
"mividaerestu2021",
"mividaerestu16",
"mividaerestu12_",
"mividaerestu10",
"mividaerestu.amor",
"mividaerestu-18",
"mividaerestU1",
"mividaerest(U)",
"mividaeresfrank",
"mividaeres tu",
"mividaentusmanos",
"mividaentera1","mividaentera01","mividaenrosayael",
"mividaenrosa","mividaelrock@hotmail.com",
"mividaelparaiso","mividaeamo","mividadura","mividadiva","mividadios",
"mividadieguis","ividadetrasdelatuya","mividaderstu",
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
senha3 = random.choice(list3)	
listname = random.choice(name)
listname2 =  random.choice(name2)
listname3 =  random.choice(name3)
listname4 =  random.choice(name3)

print(f'''{G}*Criador Cl4y
{R}████████╗ ██████╗  ██████╗ ██╗     ███████╗
{B}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{C}   ██║   ██║   ██║██║   ██║██║     ███████╗
{Y}   ██║   ██║   ██║██║   ██║██║     ╚════██║
{RT}   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{R}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {G}V.Beta.1
{G} Obrigado a todos, pelo o uso dessa ferramenta{C} !''')

sleep(1)
print()
print(f'''{R}#########################################################{C}''')
sleep(1)
print (f'''{Y}#############  {B}[ 1{G} ✓{B} ] {G} CPF.{Y}             ###############{C}''')
sleep(1)
print()
print (f'''{Y}#############  {B}[ 2{G} ✓{B} ] {G} Gerar CCFUL.{Y}      ###############{C}''')
sleep(1)
print()
print (f'''{Y}#############  {B}[ 3{G} ✓{B} ] {G} Bin Válida.{Y}       ###############{C}''')
sleep(1)
print()
print (f'''{Y}#############  {B}[ 4{G} ✓{B} ] {G} Gerar CPF e SENHA.{Y}###############{C}''')
sleep(1)
print()
print (f'''{Y}#############  {B}[ 5{G} ✓{B} ] {G} CVV.{Y}              ###############{C}''')
sleep(1)
print()
print (f'''{Y}#############  {B}[ 6{G} ✓{B} ] {G} Gerar NOME.{Y}       ###############{C}''')
sleep(1)
print()
print (f'''{Y}#############{B}  [ 0{G} ✓{B} ] {G} Sair do Programa.{Y} ###############{C}''')
sleep(1)
print()
print(f'''{R}#########################################################{C}''')
print()
sleep(1)
opcao = int(input(f''' {Y} Qual foi a sua Escolha:--> {C} '''))
clear()

if opcao == 1:

 opcao = int(input(f'''{R}[7]{B} Validar um CPF
{R}[8]{B} Gerar um CPF válido{C}
 {Y} opção:-->  {C}'''))


 if opcao == 7:
    cpf = input('Digite o CPF sem pontos e traços:-->  ')
    if cpf_validate(cpf):
        print(f'''#############  {B}[ {G} ✓{B} ] {G} CPF Válido:-->{C}       ###############.''')
        sleep(3)
    else:
        print(f'''#############  {R}[ ✓ ] CPF Inválido:-->{C}       ###############.''')
elif opcao == 8:
    cpf = cpf_generate()
    if cpf_validate(cpf):
        print(f'''############# {G} CPF Gerado:--> {C} {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} ###############''')
        

if opcao == 2:
	
 
    print(f'''{Y}############# {G} Nome do Cadastrado:-->  {C}''' , listname, listname2, listname3, listname4 )
    sleep(1)
    print(f'''{Y}############# {G} Número do cartão:--> {C}''', binlist1,nume2)
    sleep(2)
    print(f'''{Y}############# {G} Cvv do cartão:-->  {C}''',cvv)
    sleep(3)
    print(f'''{Y}############# {G} Data do cartão:--> {C}''', data1, data2, data3)

   
if opcao == 3:
	print(f'''{Y}############# {G} BIN Válida:-->  {C}''',binlist1)
if opcao == 4:

	print (f'''{Y}#############{G} Senha:-->  {C}''', senha3)
	   
if opcao == 5:
	print (f'''{Y}#############{G} CVV:-->  {C}''', cvv)
	
if opcao == 6:	
 	
	print (f'''{Y}#############{G} Nome:-->  {C}''', listname, listname2, listname3, listname4, data1, data2, data3)
	sleep(2)
if opcao == 0:

	print("Finalizado Script ")

	exit()

	print("=-=" * 10)

print("Fim do Programa! Volte Sempre!!")	
