def calcularDistanciaPercorrida():
    velocidadeInicialMs = float(input("Digite a velocidade inicial em m/s: "))
    aceleracaoMs2 = float(input("Digite a aceleração em m/s²: "))
    tempoS = float(input("Digite o tempo em segundos: "))

    distanciaM = velocidadeInicialMs * tempoS + 0.5 * aceleracaoMs2 * tempoS ** 2
    return distanciaM

distanciaPercorridaM = calcularDistanciaPercorrida()
print(f"A distância percorrida pelo veículo durante esse intervalo de tempo é de {distanciaPercorridaM} metros.")
