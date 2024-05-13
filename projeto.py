def salvar_instrucoes_arquivo(instrucoes_binarias, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        for instrucao_binaria in instrucoes_binarias:
            arquivo_saida.write(instrucao_binaria + '\n')  # Adicionando '\n' para quebrar linha
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
        instrucao = linha.strip() 
        instrucoes.append(instrucao)
    return instrucoes
 
def converter_para_binario(instrucoes_hex):
    instrucoes_binarias = []
    for instrucao_hex in instrucoes_hex:
        instrucao_binaria = bin(int(instrucao_hex, 16))[2:].zfill(32)  
        instrucoes_binarias.append(instrucao_binaria)
    return instrucoes_binarias

def obter_registradores_modificados(instrucao_binaria):
    # Lógica para obter os registradores modificados por uma instrução
    # Substitua esta lógica pela implementação específica para sua arquitetura
    # Esta é uma implementação fictícia
    return []

def obter_registradores_usados(instrucao_binaria):
    # Lógica para obter os registradores usados por uma instrução
    # Substitua esta lógica pela implementação específica para sua arquitetura
    # Esta é uma implementação fictícia
    return []

def detectar_conflitos(instrucoes_binarias):
    instrucoes_com_nop = []

    # Itera sobre todas as instruções
    for i, instrucao_atual in enumerate(instrucoes_binarias):
        # Adiciona a instrução atual à lista de instruções com NOPs
        instrucoes_com_nop.append(instrucao_atual)

        # Verifica se a instrução atual depende do resultado de alguma instrução anterior
        for j in range(i):
            instrucao_anterior = instrucoes_binarias[j]
            # Identifica os registradores modificados pela instrução anterior
            registradores_modificados_anterior = obter_registradores_modificados(instrucao_anterior)
            # Identifica os registradores usados pela instrução atual
            registradores_usados_atual = obter_registradores_usados(instrucao_atual)
            
            # Verifica se há uma sobreposição entre os registradores modificados pela instrução anterior
            # e os registradores usados pela instrução atual
            # Aqui, estou assumindo que há um conflito se houver qualquer sobreposição entre os registradores
            if any(registro in registradores_usados_atual for registro in registradores_modificados_anterior):
                # Se houver um conflito, adicione uma instrução NOP à lista de instruções com NOPs
                instrucoes_com_nop.append("00000000000000000000000000000000")
                break  # Não é necessário verificar as instruções anteriores se um conflito foi encontrado

    return instrucoes_com_nop


def aplicar_tecnica(instrucoes_binarias, tempo_clock):
    instrucoes_com_nop = detectar_conflitos(instrucoes_binarias)
    return instrucoes_com_nop

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
    # ler as linhas
    instrucoes_hex = ler_instrucoes(arquivo_ROM)

    #  Converter para binário
    instrucoes_binarias = converter_para_binario(instrucoes_hex)

    # Aplicar a técnica
    instrucoes_otimizadas = aplicar_tecnica(instrucoes_binarias, tempo_clock)

    # Arquivo novo
    nome_arquivo_saida = input("Digite o nome do arquivo de saída para as instruções otimizadas: ")
    salvar_instrucoes_arquivo(instrucoes_otimizadas, nome_arquivo_saida)

    # Resultado
    exibir_resultado(instrucoes_otimizadas)
else:
    print("Não foi possível prosseguir devido a erros na abertura do arquivo.")
