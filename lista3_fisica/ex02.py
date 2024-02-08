'''
    2. Determinar a força de atrito necessária para manter um objeto 
    em repouso em uma superfície horizontal, dado o coeficiente de 
    atrito e a força normal.
'''


coeficiente_atrito = float(input("Digite o coeficiente de atrito: "))
forca_normal = float(input("Digite a força normal: "))

forca_atrito = coeficiente_atrito * forca_normal

print(f"A força de atrito necessária é: {forca_atrito} N")
