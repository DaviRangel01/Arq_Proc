def abrir_ROM(nome_arquivo):
    try:
        arquivo_ROM = open(nome_arquivo, 'r')
        return arquivo_ROM
    except FileNotFoundError:
        print("O arquivo de memória de instrução (ROM) não foi encontrado.")
        return None
    except Exception as e:
        print("Ocorreu um erro ao tentar abrir o arquivo de memória de instrução (ROM):", e)
        return None

def ler_instrucoes(arquivo_ROM):
    instrucoes = []
    for linha in arquivo_ROM:
        instrucao = linha.strip()  # Remove espaços em branco e quebras de linha
        instrucoes.append(instrucao)
    return instrucoes

def converter_para_binario(instrucoes_hex):
    instrucoes_binarias = []
    for instrucao_hex in instrucoes_hex:
        # Converter instrução hexadecimal para binário
        instrucao_binaria = bin(int(instrucao_hex, 16))[2:].zfill(32)  # 32 bits, preenchidos com zeros a esquerda
        instrucoes_binarias.append(instrucao_binaria)
    return instrucoes_binarias

def fechar_ROM(arquivo_ROM):
    arquivo_ROM.close()

def aplicar_tecnica(instrucoes_binarias, tempo_clock):
    # implementa técnica para melhorar o desempenho
    
    return instrucoes_binarias

def salvar_instrucoes_arquivo(instrucoes_binarias, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        for instrucao_binaria in instrucoes_binarias:
            arquivo_saida.write(instrucao_binaria + '\n')

def exibir_resultado(instrucoes_binarias):
    print("Instruções convertidas para binário:")
    for instrucao_binaria in instrucoes_binarias:
        print(instrucao_binaria)

#  Inserir o tempo de clock do Pipeline
tempo_clock = float(input("Insira o tempo de clock do Pipeline: "))

# Escolher o arquivo com o programa em binário ou hexadecimal
nome_arquivo = input("Digite o nome do arquivo com o programa em binário ou hexadecimal: ")
arquivo_ROM = abrir_ROM(nome_arquivo)

if arquivo_ROM:
    # Ler cada linha do arquivo e armazenar as instruções
    instrucoes_hex = ler_instrucoes(arquivo_ROM)

    #  Converter cada instrução para o formato binário
    instrucoes_binarias = converter_para_binario(instrucoes_hex)

    #  Aplicar a técnica e calcular o desempenho
    instrucoes_otimizadas = aplicar_tecnica(instrucoes_binarias, tempo_clock)

    #  Gerar um arquivo novo com a aplicação da técnica
    nome_arquivo_saida = input("Digite o nome do arquivo de saída para as instruções otimizadas: ")
    salvar_instrucoes_arquivo(instrucoes_otimizadas, nome_arquivo_saida)

    # Exibir o resultado
    exibir_resultado(instrucoes_otimizadas)
else:
    print("Não foi possível prosseguir devido a erros na abertura do arquivo.")
