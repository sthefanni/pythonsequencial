
t = input("insira o tamanho do arquivo em MB: ")
v = input("Informe a velocidade em Mbps: “)
s = t * 8 / v
m = ( s/ 60)
s = segundos % 60
print ‘o tempo de download equivale a’, m, ‘minutos e’, s, ‘segundos’
