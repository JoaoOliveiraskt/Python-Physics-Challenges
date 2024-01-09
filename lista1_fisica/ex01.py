def calcularVelocidadeMedia(deslocamentoTotal, tempoTotal):

  velocidadeMedia = deslocamentoTotal / tempoTotal
  print(f'A velocidade média é {velocidadeMedia} m/s')

deslocamentoTotal = float(input("Digite o deslocamento em metros: "))
tempoTotal = float(input("Digite o tempo em segundos: "))


calcularVelocidadeMedia(deslocamentoTotal, tempoTotal)