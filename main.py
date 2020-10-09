
import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as M
from scipy import io
import Amostras
from control import *

#--------------------------------Amostras----------------------------------

#Pegando as amostras de um  arquivo txt
#degrau0_2 = open('degrau0_2.txt', 'r')
#resp0_2 = open('resp0_2.txt', 'rb')
#tempo0_2 = open('tempo0_2.txt', 'r')

#Pegando a amostra direto em formato Matlab
mydata = io.loadmat('amostras_equipe6.mat') #Tenho o vetor degrau0_2,  resp0_2 e tempo0_2 dentro da amostra
degrau = mydata['degrau0_2']
resp = mydata['resp0_2']
tempo = mydata['tempo0_2']

C = len(degrau[0])
L = len(degrau) 

F = np.array([resp[0,0:C-1], degrau[0,0:C-1]],)
F = F.T

J = np.array([resp[0,0:C-1],])
J = J.T

#C = len(J[0])
#L = len(J) 
#print("coluna ", C)
#print("linha ",L)

Theta = F.T @ F
Theta = np.linalg.inv(Theta)
Theta = Theta @ F.T @ J

#print(Theta)

a1 = Theta[0]
b1 = Theta[1]

sysZ = TransferFunction(b1,(1-a1),0.2)

#print(sysZ)

#plt.plot(tempo,espmq)
#plt.show

# ----------------------------------PID-------------------------------------
#a1 = 0.99557
#b1 =  0.0037426

#Kp = 4     #Ganho proporcional
#Ki = 0.1   #Ganho integral
#Kd = 1     #Ganho derivativo

#Ts = 0.1   #Tempo 

#SP = 50    #Setpoint
#PV = 0     #Precess Value

#resposta = 0 
#AcaoIntegral = 0

#ErroAnterior = SP - PV

#for i in np.arange(0.1, 200, 0.1): #o i vai de 0.1 até 100 passo 0.1

# Erro = SP - PV

#  AcaoProporcional = Kp*Erro
#  AcaoIntegral = AcaoIntegral + Ki*Ts*Erro
#  AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd

#  AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa

#  PV = a1*PV + b1*AcaoControlador
#  resposta = [resposta, PV]
    
  #print(resposta)
  #plt.plot(i, PV)

#plt.show()