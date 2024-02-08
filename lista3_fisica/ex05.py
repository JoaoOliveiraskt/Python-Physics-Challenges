'''
    5. Calcular a força normal exercida sobre um objeto em um elevador 
    acelerado verticalmente, levando em consideração a massa do objeto 
    e a aceleração do elevador.
'''


massa_objeto = float(input("Digite a massa do objeto (em kg): "))
aceleracao_elevador = float(input("Digite a aceleração do elevador (em m/s²): "))

gravidade = 9.8
forca_normal = massa_objeto * (aceleracao_elevador + gravidade)

print("A força normal exercida sobre o objeto é:", forca_normal, "N")

