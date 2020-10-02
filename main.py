
import numpy as np
import matplotlib.pyplot as plt
from scipy import io
import Amostras

#--------------------------------Amostras----------------------------------

#Pegando as amostras de um  arquivo txt
degrau0_2 = open('degrau0_2.txt', 'r')
resp0_2 = open('resp0_2.txt', 'rb')
tempo0_2 = open('tempo0_2.txt', 'r')

#Pegando a amostra direto em formato Matlab
mydata = io.loadmat('amostras_equipe6.mat') #Tenho o vetor degrau0_2,  resp0_2 e tempo0_2 dentro da amostra
degrau = mydata['degrau0_2']
resp = mydata['degrau0_2']
tempo = mydata['tempo0_2']

#print(np.size(degrau))

C = len(degrau[0])
L = len(degrau) 

if (L > 1): #Número de linhas do vetor coluna
  F = [resp(1:L-1,1), degrau(1:L-1,1)]
  J = [resp(2:L,1)]

elif (C > 1): #Número de colunas do vetor linha
  F = [resp(1,1:C-1), degrau(1,1:C-1)]
  J = [resp(1,2:C)]


# ----------------------------------PID-------------------------------------

a1 =  0.99557
b1 =  0.0037426

Kp = 4     #Ganho proporcional
Ki = 0.1   #Ganho integral
Kd = 1     #Ganho derivativo

Ts = 0.1   #Tempo 

SP = 50    #Setpoint
PV = 0     #Precess Value

resposta = 0 
AcaoIntegral = 0

ErroAnterior = SP - PV

for i in np.arange(0.1, 100, 0.1): #o i vai de 0.1 até 100 passo 0.1

  Erro = SP - PV

  AcaoProporcional = Kp*Erro
  AcaoIntegral = AcaoIntegral + Ki*Ts*Erro
  AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd

  AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa

  PV = a1*PV + b1*AcaoControlador
  resposta = [resposta, PV]
  
  #print(resposta)

  #plt.plot(i, resposta)
  #plt.show()