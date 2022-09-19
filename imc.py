peso = int(input("Seu peso: "))
altura = float(input("Sua altura: "))

def imcCalc(p, a):
    alturaAoQuadrado = a * a
    calculo = p / alturaAoQuadrado
    return calculo


print(round(imcCalc(peso, altura), 1))