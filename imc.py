peso = int(input("Seu peso: "))
altura = float(input("Sua altura: "))

def imcCalc(p, a):
    alturaAoQuadrado = a * a
    calculo = p / alturaAoQuadrado
    return calculo

resultadoImc = round(imcCalc(peso, altura), 1)

if resultadoImc < 17: 
    print(resultadoImc, "Muito abaixo do peso")
elif resultadoImc >= 17 and resultadoImc <= 18.49:
    print(resultadoImc, "Abaixo do peso")
elif resultadoImc >= 18.50 and resultadoImc <= 24.99:
    print(resultadoImc, "Abaixo do peso")
elif resultadoImc >= 25 and resultadoImc <= 29.99:
    print(resultadoImc, "Acima do peso")
elif resultadoImc >= 30 and resultadoImc <= 34.99:
    print(resultadoImc, "Obesidade I")
elif resultadoImc >= 35 and resultadoImc <= 39.99:
    print(resultadoImc, "Obesidade II (Severa)")
elif resultadoImc > 40:
    print(resultadoImc, "Obesidade III (Mórbida)")
