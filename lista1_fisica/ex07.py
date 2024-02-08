def calcularDistanciaPercorrida(velocidadeMedia, tempoH):
    distanciaKm = velocidadeMedia * tempoH
    return distanciaKm

velocidadeMedia = float(input("Digite a velocidade média em km/h: "))
tempoH = float(input("Digite o tempo em horas: "))

distanciaPercorrida = calcularDistanciaPercorrida(velocidadeMedia, tempoH)
print(f"A distância percorrida pelo veículo foi de {distanciaPercorrida} quilômetros.")
