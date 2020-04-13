import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo de procura: ')

def Format_zize(tamanho):
    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5

    if tamanho < kilo:
        texto = 'Byte'
    elif tamanho < mega:
        tamanho /= kilo
        texto = "Kb"
    elif tamanho < giga:
        tamanho /= mega
        texto = "Mb"
    elif tamanho < tera:
        tamanho /= giga
        texto = "Gb"
    elif tamanho < peta:
        tamanho /= tera
        texto = "Tb"
    else:
        tamanho /= peta
        texto = "P"
    
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')

count = 0
# Percorre dentro da raiz do caminho_procura
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                count += 1
                caminho_completo = os.path.join(raiz, arquivo) # Caminho com nome e extensao dos arquivos
                nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                tamanho = os.path.getsize(caminho_completo)
                print()

                print('Encontrei o arquivo: ', arquivo)
                print('caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado ',Format_zize(tamanho))
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print(f'{count} arquivo(s) encontrado(s)')