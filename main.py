
#Pegando as amostras de um  arquivo txt
degrau0_2 = open('degrau0_2.txt', 'r')
resp0_2 = open('resp0_2.txt', 'r')
tempo0_2 = open('tempo0_2.txt', 'r')

#Usando o metodo dos Minimos Quadrados
[L, C] = size(resp0_2); #Pegando a linha (L) e coluna (C) da amostra de resposta

if L > 1:
    F = [resp0_2(1:L-1,1) degrau0_2(1:L-1,1)];
    J = [resp0_2(2:L,1)];