x = input(“insira quanto você ganha por hora trabalhada: “)
h = input(“insira o número de horas trabalhadas: “)

s = x* h

ir = 11/100.0 *s
inss = 8/100.0 * s
sindicato = 5/100.0 * s

r = ir + inss + sindicato
sl = s - r

print 'seu salário bruto eh igual a',s

print 'valor dos impostos:'
print 'IR: ',ir
print 'INSS: ',inss
print 'sindicato: ',sindicato

seu salário liquido eh igual a: ',sl