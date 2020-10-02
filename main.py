
import numpy as np
import matplotlib.pyplot as plt

#Pegando as amostras de um  arquivo txt
degrau0_2 = open('degrau0_2.txt', 'r')
resp0_2 = open('resp0_2.txt', 'rb')
tempo0_2 = open('tempo0_2.txt', 'r')
 
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
  
  #plt.plot(i, resposta)
  #plt.show()