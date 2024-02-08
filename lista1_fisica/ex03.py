def distanciaArrmessadorRebatedor(velocidade, tempo):

  distancia = velocidade * tempo
  print(f'A distância entre o arremessador e o rebatedor é {distancia} metros')

velocidade = float(input("Digite a velocidade da bola em m/s: "))
tempo = float(input("Digite o tempo em segundos: "))

distanciaArrmessadorRebatedor(velocidade, tempo)