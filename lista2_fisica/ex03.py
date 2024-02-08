def calcularVelocidadeMediaDoMotorista():
    distanciaTotal = 100
    tempoTotalH = 1.5
    velocidade1 = 90
    velocidade2 = 80

    distanciaRestante = distanciaTotal - 30 - 40
    tempoRestanteH = tempoTotalH - 30 / velocidade1 - 40 / velocidade2
    velocidadeMedia = distanciaRestante / tempoRestanteH

    print(f"A velocidade média do motorista no último trecho foi de {velocidadeMedia:.2f} km/h.")

calcularVelocidadeMediaDoMotorista()
