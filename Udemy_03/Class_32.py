import time


def calcular_tempo_execucao(funcao):
    def wrapper(*args):
        print(*args)
        inicio = time.time()
        resultado = funcao(*args)
        fim = time.time()
        print(f"A função '{funcao.__name__}' levou {fim - inicio:.2f} segundos para executar.")
        return resultado
    return wrapper


@calcular_tempo_execucao
def funcao_demorada(segundos):
    time.sleep(segundos)
    print(f"Aguardou {segundos} segundos.")


# Chamando a função decorada
funcao_demorada(3)
