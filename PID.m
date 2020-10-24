a1 = 0.9956;
b1 = 0.003743;

Kp = 13;
Ki = 0.5;
Kd = 1;

Ts = 0.2;

SP = 50; %Sinal de entrada

tempo = 0:0.2:350;

%------------------------------Malha Aberta-------------
PV = 0;  %Sinal de saída
resp_MA = 0;
for i = 0.1:0.2:350
  PV = a1*PV + b1*SP;
  resp_MA = [resp_MA PV];
end
%plot(tempo,resp_MA)

%------------------------------#Malha Fechada sem Ganho Proporcional-------------
PV = 0;  %Sinal de saída
resp_MF = 0;
for i = 0.1:0.2:350
  Erro = SP - PV;
  PV = a1*PV + b1*Erro;
  resp_MF = [resp_MF PV];
end
%plot(tempo,resp_MF)

%--------------------------------Malha Fechada com Controlador PID

AcaoIntegral = 0;
ErroAnterior = SP - PV;

PV = 0;  %Sinal de saída
resp_PID = 0;
for i = 0.1:0.2:350
  
  Erro = SP - PV;
  
  AcaoProporcional = Kp*Erro;
  AcaoIntegral = AcaoIntegral + Ki*Ts*Erro;
  AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd;
  
  ErroAnterior  = Erro;
  
  AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa;
  
  PV = a1*PV + b1*AcaoControlador;
  resp_PID = [resp_PID PV];
 
end

%plot(tempo,resp_PID)
plot(tempo, resp_MA, tempo, resp_MF, tempo, resp_PID);
