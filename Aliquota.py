name = str(input('Qual seu nome?\n'))

muss = float(input('Insira a quantidade de Mussarela em kg:\n'))
muss1 = (22.60 * muss) *  0.05

mort = float(input('Insira a quantidade de Mortadela em kg:\n'))
mort1 = (8.98 * mort) * 0.065

pre = float(input('Insira a quantidade de Presunto em kg:\n'))
pre1 = (31.03 * pre) * 0.045

peito = float(input('Insira a quatidade de Peito de Peru em kg:\n'))
pei = (58.90 * peito) * 0.025

print('Aliquota da Mussarela é:', muss1)
print('Aliquota da Mortadela é:', mort1)
print('Aliquota do Presunto é:', pre1)
print('Aliquota do Peito de Peru é:', pei)

total = pei + muss1 + mort1 + pre1

print(name, 'Sua comissão final é:', total)