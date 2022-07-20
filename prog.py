from math import sqrt

reg1 = [('robo1', 1, (5, 8), 4), ('robo2', 2, (5, 4), 4), ('robo3', 3, (2, 2), 1), ('robo1', 4, (4, 9), 4), ('robo3', 5, (1,3), 3), ('robo4', 6, (7, 5), 3), ('robo5', 7, (8, 6), 1), ('robo1',8, (3, 2), 4), ('robo2', 9, (1, 8), 4)]

# --------- LETRA A --------- 

def distancia(p1, p2):
  def dx(): return p1[0] - p2[0]
  def dy(): return p1[1] - p2[1]
  return sqrt(dx()**2 + dy()**2)

def calculaDistancia(idx, i, entrada, robo):
    if idx-1 < 0:
        return distancia(i, (0,0))
    else:
        return distancia(i, list([x[2] for x in entrada if x[0] == robo])[idx-1])

def distPercorridaRobo(robo, entrada):
    print(sum(list([calculaDistancia(idx,i,entrada,robo) for idx,i in enumerate(list([x[2] for x in entrada if x[0] == robo]))])))
        
#distPercorridaRobo('robo1', reg1)


# --------- LETRA B --------- 

def roboMaiorDistFinalOrigem(entrada):
    lista = (list(set(x for x in entrada if x[1] == max(y[1] if x[0] == y[0] else x[1] for y in entrada))))

    print(max(lista, key=lambda x: distancia((0,0), x[2]))[0])

#roboMaiorDistFinalOrigem(reg1)


# --------- LETRA C --------- 

def distPercorridaRoboC(robo, entrada):
    return sum(list([calculaDistancia(idx,i,entrada,robo) for idx,i in enumerate(list([x[2] for x in entrada if x[0] == robo]))]))

def caminhosRobos(entrada):
    #retorna o caminho feito em x e y para cada robo
    def caminhoRobo(robo, entrada):
        return list([distPercorridaRoboC(robo, entrada)] + [(0,0)] + [x[2] for x in entrada if x[0] == robo])
        
    print(sorted(list([x] + caminhoRobo(x, entrada) for x in list(set(x[0] for x in entrada))), key=lambda x: x[1]))

caminhosRobos(reg1)

# --------- LETRA D --------- 

def roboIdentificaMaisVitimas(entrada):
    print(max(list(set(x[0] for x in entrada)), key=lambda x: sum(y[3] for y in entrada if y[0] == x)))
    

# roboIdentificaMaisVitimas(reg1)