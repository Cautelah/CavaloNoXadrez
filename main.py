import numpy as np
n = 8 #tamanho do tabuleiro
solucao = 0 #contagem de soluções
tabuleiro = np.array([[0] * n for i in range(n)])

def e_valido(tabuleiro, linha, coluna): 
    #checa se é possível mover para essa posição)
    if linha >= n or coluna >= n:
        return False
    elif linha < 0 or coluna < 0:
        return False
    elif tabuleiro[linha][coluna] != 0:
        return False
    else:
        return True


def pegar_validos( 
        tabuleiro,
        linha,
        coluna,
        movimentos_legais
):
    #verifica todas as posições possíveis
    return [(i, j) for i, j in movimentos_legais
            if e_valido(tabuleiro, linha + i, coluna + j)]


def warnsdorff(tabuleiro, linha, coluna, movimentos_legais):
    #utiliza heurística Warnsdorff para priorizar movimentos que direcionam para a posição com menor movimentos possíveis
    
    proximos_movimentos = [(i, j) for i, j in pegar_validos(
        tabuleiro, linha, coluna, movimentos_legais)]
    #vê todos os movimentos
    
    com_proximos_movimentos = [ (len(pegar_validos(tabuleiro, linha + i, coluna + j, movimentos_legais)), i, j) for i, j in proximos_movimentos]
    #calcula a quantidade de movimentos possíveis
    
    return [(t[1], t[2]) for t in sorted(com_proximos_movimentos)]
    #retorna em ordem crescente


def utilitario(tabuleiro, atual_x, atual_y, movimentos_legais,caminho):
    global solucao
    if caminho > n**2:
        #se percorreu o tabuleiro todo, finalize
        return True
    for i,j in warnsdorff(tabuleiro, atual_x, atual_y, movimentos_legais):
      novo_x = atual_x + i
      novo_y = atual_y + j
      tabuleiro[novo_x][novo_y] = caminho
      if (0 in tabuleiro):
          utilitario(tabuleiro, novo_x, novo_y, movimentos_legais,
                      caminho + 1)
      else:
          solucao += 1
          print("Solução: ",solucao,"\n",tabuleiro)
          if solucao == 1:
            input("Aperte enter para encontrar mais soluções")
      tabuleiro[novo_x][novo_y] = 0
    return False


def solucionar(tabuleiro,x_inicial=0,y_inicial=0):
    tabuleiro[x_inicial][y_inicial] = 1  #inicia na posição [0][0]
    caminho = 2


    movimentos_legais = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    #  movimento_x = [2, -1,-1, 2,-2, 1, 1,-2]
    #  movimento_y = [1, -2, 2,-1,-1, 2,-2, 1]

    if (not utilitario(tabuleiro, x_inicial, y_inicial,movimentos_legais, caminho)):
        print("Não há mais soluções possíveis")
    


solucionar(tabuleiro)
