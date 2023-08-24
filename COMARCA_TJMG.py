from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
import time

text_content = ""

def carregarPDF():
    while True:
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        arquivo_pdf = askopenfilename()
        if arquivo_pdf == "":
            print("Aperte 'ENTER' para selecionar outro arquivo")
            menu_carrregar_pdf2 = input("> ")
            if menu_carrregar_pdf2 == "":
                time.sleep(0.2)
                continue
        else:
            break
    with open(arquivo_pdf, "rb") as arquivo_pdf:
        print("Carregando o arquivo, isso pode levar algus instantes......................\n")
        time.sleep(0.2)
        pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
        global text_content
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()
    
    return text_content
        

def pesquisarnome():
    global text_content
    while True:
        print("Digite o nome do cidadão (ou 'sair' para voltar): ")
        nome = input("> ")
        print()
        time.sleep(0.2)
        
        if nome.lower() == 'sair':
            break
        
        if nome.upper() in text_content:
            print("-----------------------------------")
            print("|    ESTÁ NA LISTA DA COMARCA     |")
            print("-----------------------------------")
            print()
            time.sleep(0.2)
            print("****************************************************************************\n")
        else:
            print("-----------------------------------")
            print("|  NÃO ESTÁ NA LISTA DA COMARCA   |")
            print("-----------------------------------")
            print()
            print("****************************************************************************\n")
        
        while True:
            time.sleep(0.2)
            print("-----------------------------------")
            time.sleep(0.1)
            print("|       O que deseja fazer:       |")
            time.sleep(0.1)
            print("-----------------------------------")
            time.sleep(0.1)
            print("| 1- Pesquisar novamente          |")
            time.sleep(0.1)
            print("| 2- Voltar para o menu principal |")
            time.sleep(0.1)
            print("-----------------------------------")
            print()
            time.sleep(0.2)
            
            print("Digite apenas o número da opção: ")
            menu_pesquisar_nome = int(input("> "))
            print()
            time.sleep(0.2)

            if menu_pesquisar_nome not in [1, 2]:
                print("---------------------------------------")
                print("| Número incorreto, digite novamente! |")
                print("---------------------------------------")
                print()
                print("****************************************************************************\n")
            elif menu_pesquisar_nome == 2:
                return
            else:
                break

while True:
    print()
    print("------------------------------- LISTA COMARCA ------------------------------\n")
    time.sleep(0.2)

    print("Aperte 'ENTER' para seleccionar o arquivo PDF\nou digite 'sair' para sair do sistema:\n")
    menu_prncipal = input("> ")
    print()
    time.sleep(0.2)

    if menu_prncipal == "":
        carregarPDF()
    elif menu_prncipal != "sair":
        print("---------------------------------------")
        print("|           Digite novamente!         |")
        print("---------------------------------------")
        print()
        continue
    elif menu_prncipal.lower() == "sair":
        print("Saindo............................\n")
        time.sleep(0.2)
        break
    print("------------------------------------------------------------------------------\n")
    time.sleep(0.2)

    pesquisarnome()

    while True:
        print("-----------------------------------")
        time.sleep(0.1)
        print("|        O que deseja fazer:      |")
        time.sleep(0.1)
        print("-----------------------------------")
        time.sleep(0.1)
        print("| 1- Carregar outro PDF           |")
        time.sleep(0.1)
        print("| 2- Sair                         |")
        time.sleep(0.1)
        print("-----------------------------------")
        time.sleep(0.1)
        print()
        print("Digite apenas o número da opção:")
        menu_carrregar_pdf = int(input("> "))
        print()
        print("****************************************************************************\n")
        time.sleep(0.1)

        if (menu_carrregar_pdf > 2) or (menu_carrregar_pdf < 1):
            print("---------------------------------------")
            print("| Número incorreto, digite novamente! |")
            print("---------------------------------------")
            continue
        elif menu_carrregar_pdf == 1:
            break
        elif menu_carrregar_pdf == 2:
            print("Saindo............................\n")
            time.sleep(0.2)
            break
    if menu_carrregar_pdf == 1:
        continue
    elif menu_carrregar_pdf == 2:
        break


