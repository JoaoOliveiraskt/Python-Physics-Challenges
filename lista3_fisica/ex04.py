'''
    4. Determinar o coeficiente de atrito entre duas superfícies, dado o 
    peso do objeto e a força de atrito necessária para mantê-lo em 
    movimento constante.
'''


peso = float(input("Digite o peso do objeto (em Newtons): "))
forca_atrito = float(input("Digite a força de atrito necessária para manter o objeto em movimento constante: "))

coeficiente_atrito = forca_atrito / peso

print(f"O coeficiente de atrito entre as superfícies é: {coeficiente_atrito}")
