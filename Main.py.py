import time
from colorama import Fore, Style, init

init()  # Initialize the colorama library

# Cotações originais
print('-='*30)
cDolarAzul_original = float(input(f"Cotação de {Fore.GREEN}COMPRA{Style.RESET_ALL} Dolar Azul: "))
cDolarBranco_original = float(input(f"Cotação de {Fore.GREEN}COMPRA{Style.RESET_ALL} Dolar Branco: "))
cDolarCabecinha_original = float(input(f"Cotação de {Fore.GREEN}COMPRA{Style.RESET_ALL} Dolar Cabecinha: "))
cEuro_original = float(input(f"Cotação de {Fore.GREEN}COMPRA{Style.RESET_ALL} do Euro: "))
print('-='*30)
vDolarAzul_original = float(input(f"Cotação de {Fore.RED}VENDA{Style.RESET_ALL} do Dolar Azul: "))
vDolarBranco_original = float(input(f"Cotação de {Fore.RED}VENDA{Style.RESET_ALL} do Dolar Branco: "))
vDolarCabecinha_original = float(input(f"Cotação de {Fore.RED}VENDA{Style.RESET_ALL} do Dolar Cabecinha: "))
vEuro_original = float(input(f"Cotação de {Fore.RED}VENDA{Style.RESET_ALL} do Euro: "))

escolha = ''

while escolha != 'q':
    print('-='*30)
    escolha = input(f"Compra({Fore.GREEN}C{Style.RESET_ALL})/Venda({Fore.RED}V{Style.RESET_ALL}) ({Fore.MAGENTA}Q{Style.RESET_ALL} sair): ").lower()
    if escolha == 'q':
        print('Fechando...')
        time.sleep(2)
        break
    elif escolha == 'c':
        # Cópia das cotações para a transação
        cDolarAzul = cDolarAzul_original
        cDolarBranco = cDolarBranco_original
        cDolarCabecinha = cDolarCabecinha_original
        cEuro = cEuro_original

        moeda = input("Moeda (Azul/Branco/Cabe/Euro): ").lower()
        valor = input(f"Valor do cliente (Digite {Fore.CYAN}'{Style.RESET_ALL} para alterar cotação temporariamente): ")

        if valor == "'":
            print('-='*30)
            temp = True
            novo_valor = float(input(f"Digite o novo valor para cotação de {Fore.GREEN}COMPRA{Style.RESET_ALL}: "))
            if moeda == 'azul':
                cDolarAzul = novo_valor
                valor = float(input("Valor do cliente : "))
            elif moeda == 'branco':
                cDolarBranco = novo_valor
                valor = float(input("Valor do cliente : "))
            elif moeda == 'cabe':
                cDolarCabecinha = novo_valor
                valor = float(input("Valor do cliente : "))
            elif moeda == 'euro':
                cEuro = novo_valor
                valor = float(input("Valor do cliente : "))
            else:
                print("Moeda não reconhecida.")
        else:
            temp = False
            valor = float(valor)
            

        resultado = valor / cDolarAzul if moeda == 'azul' else \
                    valor / cDolarBranco if moeda == 'branco' else \
                    valor / cDolarCabecinha if moeda == 'cabe' else \
                    valor / cEuro if moeda == 'euro' else None

        if resultado is not None:
            print('-='*30)
            print(f"O cliente receberá {resultado:.2f} {moeda.capitalize()} na compra.")
            print()
            if temp == True:
                print(f"Cotação de {moeda.capitalize()} alterada para o valor inicial")
        else:
            print("Moeda não reconhecida.")

    elif escolha == 'v':
        # Cópia das cotações para a transação
        vDolarAzul = vDolarAzul_original
        vDolarBranco = vDolarBranco_original
        vDolarCabecinha = vDolarCabecinha_original
        vEuro = vEuro_original

        moeda = input("Moeda (Azul/Branco/Cabe/Euro): ").lower()
        valor = input(f"Valor do cliente (Digite {Fore.CYAN}'{Style.RESET_ALL} para alterar cotação temporariamente): ")

        if valor == "'":
            print('-='*30)
            temp = True
            novo_valor = float(input(f"Digite o novo para cotação de {Fore.RED}VENDA{Style.RESET_ALL}: "))
            if moeda == 'azul':
                vDolarAzul = novo_valor
                valor = float(input("Valor do cliente : "))
            elif moeda == 'branco':
                vDolarBranco = novo_valor
                valor = float(input("Valor do cliente : "))
            elif moeda == 'cabe':
                vDolarCabecinha = novo_valor
                valor = float(input("Valor do cliente : "))
            elif moeda == 'euro':
                vEuro = novo_valor
                valor = float(input("Valor do cliente : "))
            else:
                print("Moeda não reconhecida.")
        else:  
            temp = False
            valor = float(valor)
           

        resultado = valor * vDolarAzul if moeda == 'azul' else \
                    valor * vDolarBranco if moeda == 'branco' else \
                    valor * vDolarCabecinha if moeda == 'cabe' else \
                    valor * vEuro if moeda == 'euro' else None

        if resultado is not None:
            print('-='*30)
            print(f"O cliente receberá {resultado:.2f} Reais na venda de {moeda.capitalize()}.")
            print()
            if temp == True:
                print(f"Cotação de {moeda.capitalize()} alterada para o valor inicial")
            
        else:
            print("Moeda não reconhecida.")

    else:
        print("Escolha um valor válido.")
