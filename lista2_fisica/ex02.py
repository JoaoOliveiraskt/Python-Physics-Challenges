def calcularVelocidadeCaminhao():
    taxaDeGotas = float(input("Digite a taxa de gotejamento (gotas por segundo): "))
    distanciaEntreMarcas = float(input("Digite a distância entre marcas de gotas (metros): "))

    velocidadeCaminhao = taxaDeGotas * distanciaEntreMarcas

    print(f"A velocidade do caminhão é {velocidadeCaminhao} m/s.")

calcularVelocidadeCaminhao()

