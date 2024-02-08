def calcularTempoParaPerderComunicacao():
    distanciaMaximaComunicacaoKm = 10
    velocidadeTrem1Kmh = 300
    velocidadeTrem2Kmh = 250
    velocidadeRelativaKmh = velocidadeTrem1Kmh - velocidadeTrem2Kmh

    tempoH = (distanciaMaximaComunicacaoKm / velocidadeRelativaKmh) * 60
    return tempoH

tempoParaPerderComunicacaoMin = calcularTempoParaPerderComunicacao()
print(f"Após {tempoParaPerderComunicacaoMin:.0f} minutos, os trens perderão a comunicação.")
