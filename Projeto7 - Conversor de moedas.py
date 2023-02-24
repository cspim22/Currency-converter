# Importar bibliotecas
#Essa biblioteca faz uma consulta para ver a cotação das moedas, pelo que entendi ela busca no banco europeu
from currency_converter import CurrencyConverter
 # Chama a classe importada e a salva na variavel moeda

def inicio():
    print('Conversor universal de moedas')

# 1° Passo - leitura dos dados iniciais (valor de entrada, moeda inicial e moeda de destino)

def leitura_das_moedas():
    while True:
            try:
                valor_converter = float(input('Digite o valor que será convertido: '))
                break
            except(ValueError):
                print('O valor digitado não é numerico, por favor insira um valor numerico.')
    
    moeda_inicial = moeda_destino = None

    while moeda_inicial not in (1,2,3):
        try:
            moeda_inicial = int(input('''Digite a moeda de inicio:
                                       [1] BRL
                                       [2] USD
                                       [3] OUTRA
                                       R: '''))
        except(ValueError):
            print('Digite um valor valido para a moeda de entrada')
           

    while moeda_destino not in (1,2,3): 
        try:    
            moeda_destino = int(input('''Digite a moeda de destino:
                                       [1] BRL
                                       [2] USD
                                       [3] OUTRA
                                       R: '''))
        except(ValueError):
            print('Digite um valor valido para a moeda de destino')
        
    tratamento_das_moedas(valor_converter,moeda_inicial,moeda_destino) 

        

def tratamento_das_moedas(valor_converter,moeda_inicial,moeda_destino):
    if moeda_inicial == 1:
        moeda_inicial = 'BRL'
    
    elif moeda_inicial == 2:
        moeda_inicial = 'USD'
    
    elif moeda_inicial == 3:
        print('Você escolheu a opção OUTRA para a moeda inicial') 
        moeda_inicial =input('favor digitar a sigla da moeda desejada: ').upper()
    
    if moeda_destino == 1:
        moeda_destino = 'BRL'
    
    elif moeda_destino == 2:
        moeda_destino = 'USD'
    
    elif moeda_destino == 3:
        print('Você escolheu a opção OUTRA para a moeda de destino') 
        moeda_destino =input('favor digitar a sigla da moeda desejada: ').upper()
    
    converter = CurrencyConverter()
    moeda_convertida = converter.convert(valor_converter,moeda_inicial,moeda_destino)
    print(f'{valor_converter} {moeda_inicial} equivalem a {moeda_convertida:,.2f} {moeda_destino}')


leitura_das_moedas()
# fazer os teste apertandso enter