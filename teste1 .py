import re

def extrair_numeros(url):
    padrao = re.compile(r'(\d+)')
    numeros = padrao.findall(url)
    return ''.join(numeros)

def adicionar_numero(url, link):
    numeros = extrair_numeros(url)
    novo_url = url.replace(numeros, numeros + link)
    return novo_url

def adicionar_texto(url, novo_texto):
    novo_texto_formatado = novo_texto.replace(' ', '%20')
    novo_url = url + '?text' + novo_texto_formatado
    return novo_url

url = input('Digite número de telefone: ')

# Solicitar escolha da função
escolha = input('Escolha a função (1 para link pronto, 2 para adicionar texto): ')

# Lógica para adicionar conforme a escolha
if escolha == '1':
    link = 'https://wa.me/55'
    resultado = adicionar_numero(link, url)
elif escolha == '2':
    link2 = 'https://wa.me/55'+url
    novo_texto = input('Digite o texto a ser adicionado comesse como igual no inicio sem expasso =ola: ')
    resultado = adicionar_texto(link2, novo_texto)
else:
    resultado = 'Escolha inválida. Execute o programa novamente.'

# Exibir resultado final
print(resultado)
