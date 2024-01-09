def calcularVelocidadeMedia(distanciaKm, tempoH):
    velocidadeKmh = distanciaKm / tempoH
    velocidadeMs = velocidadeKmh / 3.6

    return velocidadeMs

distanciaKm = float(input("Digite a distância em quilômetros: "))
tempoH = float(input("Digite o tempo em horas: "))

velocidadeMedia = calcularVelocidadeMedia(distanciaKm, tempoH)

print(f"A velocidade média é {velocidadeMedia:.2f} m/s.")