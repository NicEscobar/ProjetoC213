from tkinter import *
import main as m
import numpy as np

root = Tk()
root.geometry("800x400")


def Salvar_Parametros():
    global kp
    global ki
    global kd
    global SP
    global PV
    global Ts
    global tempo2
    global tempo
    global a1
    global b1

    Theta = m.minimos_quadrados()

    a1 = Theta[0]
    b1 = Theta[1]

    kp = int(kpLabel.get())  # 13 Ganho proporcional
    ki = int(kiLabel.get())  # 0.5 Ganho integral
    kd = int(kdLabel.get())  # 1 Ganho derivativo

    SP = int(SPLabel.get())  # 50 Setpoint
    PV = int(PVLabel.get())  # 0 Precess Value

    Ts = float(tsLabel.get())  # 0.2 Tempo de amostragem
    tempo = int(xLabel.get())  # 350 Tempo do eixo x

    tempo2 = np.arange(0, tempo, Ts)


def Grafico_MA():  # Chama o grafico de malha aberta

    resposta_ma = m.malha_aberta(tempo2, a1, b1, PV, SP, Ts, tempo)
    m.grafico(tempo2, resposta_ma)


def Grafico_MF():  # Chama o grafico de malha fechada

    resposta_mf = m.malha_fechada_sem_ganho(tempo2, a1, b1, PV, SP, Ts, tempo)
    m.grafico(tempo2, resposta_mf)


def Grafico_MFG():  # Chama o grafico de malha fechada com controlador

    resposta_mfg = m.malha_fechada_controlador_PID(
        tempo2, a1, b1, PV, SP, kp, ki, kd, Ts, tempo)
    m.grafico(tempo2, resposta_mfg)


# ------------------primeiroContainer-------------------------------------------
fontePadrao = ("Arial", "10")
primeiroContainer = Frame()
primeiroContainer["pady"] = 10
primeiroContainer.pack()

titulo = Label(primeiroContainer, text="Sistemas Dinâmicos")
titulo["font"] = ("Arial", "10", "bold")
titulo.pack()
# ------------------segundoContainer-------------------------------------------

segundoContainer = Frame()
segundoContainer.pack()

SPLabel = Label(segundoContainer,
                text=" SP (Set Point) ", font=fontePadrao)
SPLabel.pack(side=LEFT)
SPLabel = Entry(segundoContainer)
SPLabel["width"] = 10
SPLabel["font"] = fontePadrao
SPLabel.pack(side=LEFT)

PVLabel = Label(segundoContainer,
                text=" PV (Precess Value) ", font=fontePadrao)
PVLabel.pack(side=LEFT)

PVLabel = Entry(segundoContainer)
PVLabel["width"] = 10
PVLabel["font"] = fontePadrao
PVLabel.pack(side=LEFT)

# ------------------terceiroContainer-------------------------------------------
terceiroContainer = Frame()
terceiroContainer.pack()

tsLabel = Label(terceiroContainer,
                text=" Ts (Tempo de Amostragem) ", font=fontePadrao)
tsLabel.pack(side=LEFT)

tsLabel = Entry(terceiroContainer)
tsLabel["width"] = 10
tsLabel["font"] = fontePadrao
tsLabel.pack(side=LEFT)

xLabel = Label(terceiroContainer,
               text=" Eixo x (Tempo(s)) ", font=fontePadrao)
xLabel.pack(side=LEFT)

xLabel = Entry(terceiroContainer)
xLabel["width"] = 10
xLabel["font"] = fontePadrao
xLabel.pack(side=LEFT)

# ------------------quartoContainer-------------------------------------------
quartoContainer = Frame()
quartoContainer.pack()

kpLabel = Label(quartoContainer,
                text=" kp (Ganho Proporcional) ", font=fontePadrao)
kpLabel.pack(side=LEFT)

kpLabel = Entry(quartoContainer)
kpLabel["width"] = 10
kpLabel["font"] = fontePadrao
kpLabel.pack(side=LEFT)

kiLabel = Label(quartoContainer,
                text=" ki (Ganho Integral) ", font=fontePadrao)
kiLabel.pack(side=LEFT)

kiLabel = Entry(quartoContainer)
kiLabel["width"] = 10
kiLabel["font"] = fontePadrao
kiLabel.pack(side=LEFT)

kdLabel = Label(quartoContainer,
                text=" kd (Ganho Derivativo) ", font=fontePadrao)
kdLabel.pack(side=LEFT)

kdLabel = Entry(quartoContainer)
kdLabel["width"] = 10
kdLabel["font"] = fontePadrao
kdLabel.pack(side=LEFT)

# ----------------------------------Botoes--------------------------------
btn_s = Button(root, text="Salvar Parametros", padx=50,
               pady=5, command=Salvar_Parametros)
btn_s.pack()

btn_ma = Button(root, text="Malha Aberta", padx=50,
                pady=5, command=Grafico_MA)
btn_ma.pack()


btn_mf = Button(root, text="Malha Fechada",
                padx=50, pady=5, command=Grafico_MF)
btn_mf.pack()


btn_mfc = Button(root, text="Malha Fechada com Controlador",
                 padx=50, pady=5, command=Grafico_MFG)
btn_mfc.pack()


root.mainloop()
