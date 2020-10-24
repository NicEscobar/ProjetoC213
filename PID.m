a1 = 0.9956;
b1 = 0.003743;

Kp = 13;
Ki = 0.5;
Kd = 1;

Ts = 0.2;

SP = 50; %Sinal de entrada
PV = 0;  %Sinal de saída

resp_6 = 0;
AcaoIntegral = 0;
ErroAnterior = SP - PV;

tempo = 0:0.2:350;

for i = 0.1:0.2:350
  Erro = SP - PV;
  
  AcaoProporcional = Kp*Erro;
  AcaoIntegral = AcaoIntegral + Ki*Ts*Erro;
  AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd;
  
  ErroAnterior  = Erro;
  
  AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa;
  
  PV = a1*PV + b1*AcaoControlador;
  resp_6 = [resp_6 PV];
 
end

plot(tempo,resp_6)
