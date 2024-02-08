def calcularTempoParaCompletarPercurso():
    distancia = float(input("Digite a distância em metros: "))
    velocidadeMedia = float(input("Digite a velocidade média em m/s: "))

    tempoSegundos = distancia / velocidadeMedia

    return tempoSegundos

tempoParaCompletarPercurso = calcularTempoParaCompletarPercurso()
print(f"O competidor demora {tempoParaCompletarPercurso:.2f} segundos para completar o percurso.")
