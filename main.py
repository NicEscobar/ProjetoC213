
import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as M
from scipy import io
from control import *

# --------------------------------Amostras----------------------------------

# Pegando as amostras de um  arquivo txt
#degrau0_2 = open('degrau0_2.txt', 'r')
#resp0_2 = open('resp0_2.txt', 'rb')
#tempo0_2 = open('tempo0_2.txt', 'r')

# Pegando a amostra direto em formato Matlab
# Tenho o vetor degrau0_2,  resp0_2 e tempo0_2 dentro da amostra
mydata = io.loadmat('amostras_equipe6.mat')
degrau = mydata['degrau0_2']
resp = mydata['resp0_2']
tempo = mydata['tempo0_2']

# -------------------------------Chama o grafico--------------------------


def grafico(tempo, y):
    plt.plot(tempo, y)
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("y")
    plt.show()


# --------------------------------Mínimos Quadrados ----------------------------------


C = len(degrau[0])  # numero de colunas
L = len(degrau)  # numero de linhas

F = np.array([resp[0, 0:C-1], degrau[0, 0:C-1]],)
F = F.T  # Matriz transposta
# print(F)

J = np.array([resp[0, 1:C], ])
J = J.T
# print(J)

tempo = np.array([tempo[0, 0:C-1], ])
#tempo = tempo.T


C = len(tempo[0])
L = len(tempo)
#print("coluna ", C)
#print("linha ", L)

#
Theta = np.linalg.inv(F.T @ F) @ F.T @ J
# print(Theta)

# coeficientes
a1 = Theta[0]
b1 = Theta[1]
# print(a1)
# print(b1


# funcao de transferencia Z
#sysZ = tf([int(b1)], [(1-int(a1)), 0.2])
# print(sysZ)

#t, y = step_response(sysS)
# print(y)

# ----------------------------------PID-------------------------------------

Kp = 3  # Ganho proporcional
Ki = 8  # Ganho integral
Kd = 10.25  # Ganho derivativo

Ts = 0.1  # Tempo

SP = 1  # Setpoint
PV = 0  # Precess Value

resposta = []
AcaoIntegral = 0

ErroAnterior = SP - PV
tempo2 = np.arange(0, 30, 0.1)

for i in np.arange(0, 30, 0.1):  # o i vai de 0.1 até 100 passo 0.1

    Erro = SP - PV

    AcaoProporcional = Kp*Erro
    AcaoIntegral = AcaoIntegral + Ki*Ts*Erro
    AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd

    ErroAnterior = Erro

    AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa

    PV = (a1*PV) + (b1*AcaoControlador)
    resposta.append(PV)

grafico(tempo2, resposta)
