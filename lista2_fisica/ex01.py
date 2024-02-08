def comprimentoDoTrem():
    velocidadeKmH = float(input("Digite a velocidade do trem em km/h: "))
    velocidadeMs = velocidadeKmH * 1000 / 3600
    
    comprimentoPonte = 90
    tempo = 4.5
    
    tempoPonto = comprimentoPonte / velocidadeMs
    tempoReal = tempo - tempoPonto
    
    comprimentoTrem = velocidadeMs * tempoReal
    print(f"O comprimento do trem é {comprimentoTrem} metros.")

comprimentoDoTrem()

