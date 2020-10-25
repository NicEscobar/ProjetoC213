
import numpy as np
import matplotlib.pyplot as plt
from scipy import io, signal
from control import *

# --------------------------------Amostras----------------------------------

# Pegando as amostras de um  arquivo txt
# degrau0_2 = open('degrau0_2.txt', 'r')
# resp0_2 = open('resp0_2.txt', 'rb')
# tempo0_2 = open('tempo0_2.txt', 'r')

# Pegando a amostra direto em formato Matlab
# Tenho o vetor degrau0_2,  resp0_2 e tempo0_2 dentro da amostra
mydata = io.loadmat('amostras_equipe6.mat')
degrau = mydata['degrau0_2']
resp = mydata['resp0_2']
tempo = mydata['tempo0_2']

# -------------------------------Graficos--------------------------


def grafico(tempo, y):  # Plota um gráfico
    plt.plot(tempo, y)
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("y")
    plt.show()


def graficos(tempo, y1, y2, y3):  # Plota mais de um gráfico
    plt.plot(tempo, y1, color='green')
    plt.plot(tempo, y2, color='red')
    plt.plot(tempo, y3, color='blue')
    plt.grid()
    plt.xlabel("Tempo [s]")
    plt.ylabel("Y[m]")
    plt.title("Sistema Dinâmico")
    plt.show()

# ----------------------------------Malha Aberta-------------------------------------


def malha_aberta(tempo, a1, b1, PV, SP):
    resposta = []
    for i in np.arange(0, 350, 0.2):
        PV = a1*PV + b1*SP
        resposta.append(PV)
    return resposta
    #grafico(tempo, resposta)

# ----------------------------------Malha Fechada com Controlador PID-------------------------------------


def malha_fechada_sem_ganho(tempo, a1, b1, PV, SP):
    resposta = []
    for i in np.arange(0, 350, 0.2):
        erro = SP - PV
        PV = a1*PV + b1*erro
        resposta.append(PV)
    return resposta
    #grafico(tempo, resposta)

# ----------------------------------Malha Fechada com Controlador PID-------------------------------------


def malha_fechada_controlador_PID(tempo, a1, b1, PV, SP, kp, ki, kd, Ts):
    resposta = []
    acao_integral = 0

    erro_anterior = SP - PV
    for i in np.arange(0, 350, 0.2):  # o i vai de 0.1 até 100 passo 0.1

        erro = SP - PV

        acao_proporcional = Kp*erro
        acao_integral = acao_integral + Ki*Ts*erro
        acao_derivativa = ((erro - erro_anterior)/Ts)*Kd

        erro_anterior = erro

        acao_controlador = acao_proporcional + acao_integral + acao_derivativa

        PV = (a1*PV) + (b1*acao_controlador)
        resposta.append(PV)
    return resposta
    #grafico(tempo, resposta)

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
# tempo = tempo.T


C = len(tempo[0])
L = len(tempo)
# print("coluna ", C)
# print("linha ", L)

#
Theta = np.linalg.inv(F.T @ F) @ F.T @ J
# print(Theta)

# coeficientes
a1 = Theta[0]
b1 = Theta[1]
# print(a1)
# print(b1

# funcao de transferencia Z
sysS = tf(b1, a1, 0.2)
# sysZ = tf([b1], [1-a1], 0.2)
# print(sysS)

# ----------------------------------Sistema-------------------------------------

Kp = 13  # Ganho proporcional
Ki = 0.5  # Ganho integral
Kd = 1  # Ganho derivativo

Ts = 0.2  # Tempo de amostragem
SP = 50  # Setpoint
PV = 0  # Precess Value

tempo2 = np.arange(0, 350, 0.2)

resposta_ma = malha_aberta(tempo2, a1, b1, PV, SP)
resposta_mf = malha_fechada_sem_ganho(tempo2, a1, b1, PV, SP)
resposta_mfc = malha_fechada_controlador_PID(
    tempo2, a1, b1, PV, SP, Kp, Ki, Kd, Ts)

# Chamando os gráficos
graficos(tempo2, resposta_ma, resposta_mf, resposta_mfc)
#grafico(tempo2, resposta_mf)
